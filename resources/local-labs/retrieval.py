"""Compare two lexical searches on a tiny synthetic handbook. Run with Python 3.12+."""
from dataclasses import dataclass
import json
import re


@dataclass(frozen=True)
class Document:
    key: str
    title: str
    passage: str
    audience: str = "public"


DOCUMENTS = (
    Document("desk", "Library desk", "The library desk opens at nine."),
    Document("loan", "Laptop loans", "Students may borrow a laptop for seven days."),
    Document("room", "Study rooms", "Reserve a room by email."),
    Document("roster", "Staff rota", "The custodian covers Sunday.", "staff"),
)

# Gold evidence for a public reader. None means there is no authorized answer.
CASES = (
    ("library desk", "desk"),
    ("borrow laptop", "loan"),
    ("reserve by email", "room"),
    ("notebook checkout", "loan"),
    ("custodian Sunday", None),
    ("parking fees", None),
)


def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def retrieve(query, documents, audience, *, include_passage):
    """Count distinct shared terms. Break ties by stable ID and abstain at zero."""
    terms = tokens(query)
    candidates = []
    for doc in documents:
        if doc.audience not in ("public", audience):
            continue
        searchable = doc.title + " " + doc.passage if include_passage else doc.title
        hits = len(terms & tokens(searchable))
        if hits:
            candidates.append((-hits, doc.key))
    candidates.sort()
    return [key for _, key in candidates]


def evaluate(cases, predictions):
    """Report counts. Hit@1 uses answerable cases, abstention uses unanswerable ones."""
    hits = answerable = correct_abstentions = unanswerable = 0
    rows = []
    for (query, gold), ranking in zip(cases, predictions, strict=True):
        first = ranking[0] if ranking else None
        if gold is None:
            unanswerable += 1
            correct_abstentions += first is None
        else:
            answerable += 1
            hits += first == gold
        rows.append({"query": query, "gold": gold, "returned": first})
    return {"hits_at_1": hits, "answerable": answerable,
            "correct_abstentions": correct_abstentions, "unanswerable": unanswerable,
            "cases": rows}


def main():
    comparisons = {"no_evidence": evaluate(CASES, [[] for _ in CASES])}
    for name, include_passage in (("title", False), ("title_and_passage", True)):
        predictions = [retrieve(query, DOCUMENTS, "public", include_passage=include_passage)
                       for query, _ in CASES]
        comparisons[name] = evaluate(CASES, predictions)
    print(json.dumps(comparisons, indent=2))


if __name__ == "__main__":
    main()
