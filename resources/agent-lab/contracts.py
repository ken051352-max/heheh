"""Local teaching controls; scripted requests, no LLM or external side effects."""

from dataclasses import dataclass
from contextlib import contextmanager
import json
import math
from pathlib import Path
import sqlite3
import time
from typing import Callable, Iterator, Mapping, Sequence
import uuid


class ContractError(ValueError):
    """A bounded, actionable error suitable for a tool-result adapter."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


@dataclass(frozen=True)
class Principal:
    """Construct from trusted authentication, never from model-supplied fields."""

    tenant: str
    tools: frozenset[str]


def _text(value: object, field: str, maximum: int = 200) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > maximum:
        raise ContractError("invalid_argument", f"{field}: use 1..{maximum} characters")
    return value


def _positive_int(value: object, field: str) -> int:
    if type(value) is not int or value <= 0:
        raise ContractError("invalid_argument", f"{field}: use a positive integer")
    return value


def _fields(arguments: object, required: set[str]) -> dict:
    if not isinstance(arguments, dict) or set(arguments) != required:
        raise ContractError("invalid_arguments", "provide exactly: " + ", ".join(sorted(required)))
    return arguments


def _payload(order_id: str, amount_cents: int) -> str:
    return json.dumps({"order_id": order_id, "amount_cents": amount_cents}, sort_keys=True)


class Store:
    """SQLite state for isolated fixture orders, approvals, replays, and facts."""

    def __init__(self, path: str | Path):
        self.path = str(path)
        with self._connect() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS orders (
                    tenant TEXT, order_id TEXT, total_cents INTEGER NOT NULL,
                    refunded_cents INTEGER NOT NULL DEFAULT 0,
                    PRIMARY KEY (tenant, order_id));
                CREATE TABLE IF NOT EXISTS approvals (
                    token TEXT PRIMARY KEY, tenant TEXT, payload TEXT, used_key TEXT);
                CREATE TABLE IF NOT EXISTS replays (
                    tenant TEXT, request_key TEXT, payload TEXT, result TEXT,
                    PRIMARY KEY (tenant, request_key));
                CREATE TABLE IF NOT EXISTS facts (
                    tenant TEXT, fact_key TEXT, value TEXT, observed_at REAL,
                    expires_at REAL, PRIMARY KEY (tenant, fact_key));
            """)

    @contextmanager
    def _connect(self) -> Iterator[sqlite3.Connection]:
        db = sqlite3.connect(self.path, timeout=5)
        db.row_factory = sqlite3.Row
        try:
            with db:
                yield db
        finally:
            db.close()

    def seed_order(self, tenant: str, order_id: str, total_cents: int) -> None:
        """Trusted fixture setup; deliberately not a model-visible tool."""
        _text(tenant, "tenant")
        _text(order_id, "order_id")
        _positive_int(total_cents, "total_cents")
        with self._connect() as db:
            db.execute("INSERT INTO orders VALUES (?, ?, ?, 0)", (tenant, order_id, total_cents))

    def approve_refund(self, tenant: str, order_id: str, amount_cents: int) -> str:
        """Trusted host records a human decision for an exact simulated action."""
        _text(tenant, "tenant")
        _text(order_id, "order_id")
        _positive_int(amount_cents, "amount_cents")
        token = uuid.uuid4().hex
        with self._connect() as db:
            db.execute("INSERT INTO approvals VALUES (?, ?, ?, NULL)",
                       (token, tenant, _payload(order_id, amount_cents)))
        return token

    def dispatch(self, principal: Principal, request: object,
                 approval_token: str | None = None) -> dict:
        """Only trusted code supplies principal and approval_token."""
        data = _fields(request, {"tool", "arguments"})
        tool = _text(data["tool"], "tool")
        if tool not in {"get_order", "refund_order"}:
            raise ContractError("unknown_tool", "choose get_order or refund_order")
        if tool not in principal.tools:
            raise ContractError("forbidden", "this caller is not allowed to invoke that tool")
        required = {"order_id"} if tool == "get_order" else {"order_id", "amount_cents", "idempotency_key"}
        arguments = _fields(data["arguments"], required)
        order_id = _text(arguments["order_id"], "order_id")
        if tool == "get_order":
            with self._connect() as db:
                row = db.execute("SELECT order_id, total_cents, refunded_cents FROM orders "
                                 "WHERE tenant=? AND order_id=?", (principal.tenant, order_id)).fetchone()
            if row is None:
                raise ContractError("not_found", "no order available for this caller")
            return dict(row)
        amount = _positive_int(arguments["amount_cents"], "amount_cents")
        key = _text(arguments["idempotency_key"], "idempotency_key")
        payload = _payload(order_id, amount)
        with self._connect() as db:
            # Serialize the absent-row case too; SELECT FOR UPDATE alone cannot do that.
            db.execute("BEGIN IMMEDIATE")
            previous = db.execute("SELECT payload, result FROM replays WHERE tenant=? AND request_key=?",
                                  (principal.tenant, key)).fetchone()
            if previous is not None:
                if previous["payload"] != payload:
                    raise ContractError("idempotency_conflict", "use a new key for a different action")
                return json.loads(previous["result"])
            approval = db.execute("SELECT tenant, payload, used_key FROM approvals WHERE token=?",
                                  (approval_token,)).fetchone()
            if (approval is None or approval["tenant"] != principal.tenant or
                    approval["payload"] != payload or approval["used_key"] is not None):
                raise ContractError("approval_required", "the trusted host must approve this exact action")
            row = db.execute("SELECT total_cents, refunded_cents FROM orders WHERE tenant=? AND order_id=?",
                             (principal.tenant, order_id)).fetchone()
            if row is None:
                raise ContractError("not_found", "no order available for this caller")
            if amount > row["total_cents"] - row["refunded_cents"]:
                raise ContractError("amount_exceeds_balance", "request no more than the remaining balance")
            result = {"status": "simulated_refund", "order_id": order_id, "amount_cents": amount}
            db.execute("UPDATE orders SET refunded_cents=refunded_cents+? WHERE tenant=? AND order_id=?",
                       (amount, principal.tenant, order_id))
            db.execute("UPDATE approvals SET used_key=? WHERE token=?", (key, approval_token))
            db.execute("INSERT INTO replays VALUES (?, ?, ?, ?)",
                       (principal.tenant, key, payload, json.dumps(result, sort_keys=True)))
            return result

    def remember(self, tenant: str, key: str, value: str, observed_at: float,
                 ttl_seconds: int | None = None) -> str:
        """Trusted event ingestion; timestamps come from the source event, not an LLM."""
        _text(tenant, "tenant")
        _text(key, "key")
        _text(value, "value", 1000)
        if type(observed_at) not in (int, float) or not math.isfinite(observed_at):
            raise ContractError("invalid_timestamp", "observed_at must be a finite Unix timestamp")
        if ttl_seconds is not None:
            _positive_int(ttl_seconds, "ttl_seconds")
        expires = observed_at + ttl_seconds if ttl_seconds is not None else None
        if expires is not None and not math.isfinite(expires):
            raise ContractError("invalid_timestamp", "expiry must be finite")
        with self._connect() as db:
            db.execute("BEGIN IMMEDIATE")
            prior = db.execute("SELECT value, observed_at, expires_at FROM facts WHERE tenant=? AND fact_key=?",
                               (tenant, key)).fetchone()
            if prior is not None:
                if observed_at < prior["observed_at"]:
                    return "ignored_stale"
                if observed_at == prior["observed_at"]:
                    if value != prior["value"] or expires != prior["expires_at"]:
                        raise ContractError("event_conflict", "same timestamp has conflicting facts; resolve at source")
                    return "replayed"
            db.execute("INSERT INTO facts VALUES (?, ?, ?, ?, ?) ON CONFLICT(tenant, fact_key) "
                       "DO UPDATE SET value=excluded.value, observed_at=excluded.observed_at, expires_at=excluded.expires_at",
                       (tenant, key, value, observed_at, expires))
        return "stored"

    def recall(self, tenant: str, key: str, now: float) -> str | None:
        with self._connect() as db:
            row = db.execute("SELECT value FROM facts WHERE tenant=? AND fact_key=? "
                             "AND (expires_at IS NULL OR expires_at>?)", (tenant, key, now)).fetchone()
        return row["value"] if row is not None else None

    def forget_tenant(self, tenant: str) -> None:
        """Trusted deletion of memory facts; no public arbitrary-delete tool."""
        with self._connect() as db:
            db.execute("DELETE FROM facts WHERE tenant=?", (tenant,))


def run_scripted(store: Store, principal: Principal, requests: Sequence[object], *,
                 max_steps: int = 8, max_seconds: float = 5,
                 clock: Callable[[], float] = time.monotonic,
                 approvals: Mapping[str, str] | None = None) -> list[dict]:
    """Dispatch fixed requests; check deadlines between calls, never claim model quality."""
    _positive_int(max_steps, "max_steps")
    if type(max_seconds) not in (int, float) or not math.isfinite(max_seconds) or max_seconds <= 0:
        raise ContractError("invalid_budget", "max_seconds must be finite and positive")
    deadline = clock() + max_seconds
    trace = []
    for step, request in enumerate(requests):
        if step >= max_steps:
            raise ContractError("step_limit", "stop: maximum number of tool attempts reached")
        if clock() >= deadline:
            raise ContractError("deadline", "stop: elapsed-time budget exhausted")
        token = None
        if isinstance(request, dict) and isinstance(request.get("arguments"), dict):
            key = request["arguments"].get("idempotency_key")
            if isinstance(key, str):
                token = (approvals or {}).get(key)
        try:
            result = store.dispatch(principal, request, token)
            trace.append({"step": step, "status": "ok", "result": result})
        except ContractError as error:
            trace.append({"step": step, "status": "error", "code": error.code, "message": str(error)})
    return trace
