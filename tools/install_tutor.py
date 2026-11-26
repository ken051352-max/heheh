"""Install the roadmap tutor for current Codex and OpenCode v2, without editing settings."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
import uuid


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "references/roadmap-map.md",
    "references/progress-and-planning.md",
    "scripts/progress.py",
)


def check_destination(path, boundary):
    """Do not overwrite redirected paths or files shared through hard links."""
    current = boundary
    for part in path.relative_to(boundary).parts:
        current = current / part
        if current.is_symlink() or current.resolve() != current:
            raise ValueError(f"Refusing redirected installation path: {current}")
    if path.exists() and (not path.is_file() or path.stat().st_nlink > 1):
        raise ValueError(f"Expected an unshared regular destination file: {path}")


def write_atomic(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=".tutor-install-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def install(root, home, *, update=False, opencode_dir=None, environ=None):
    root, home = Path(root).resolve(strict=True), Path(home).resolve(strict=True)
    env = os.environ if environ is None else environ
    if opencode_dir is None and any(env.get(key) for key in ("OPENCODE_CONFIG_DIR", "XDG_CONFIG_HOME")):
        raise ValueError("Custom OpenCode configuration detected; pass --opencode-dir with its config directory")
    config = Path(opencode_dir).expanduser().resolve() if opencode_dir else home / ".config/opencode"
    # A supplied config directory is an explicit destination, never a settings file.
    if config.exists() and not config.is_dir():
        raise ValueError(f"Expected OpenCode configuration directory: {config}")
    if not (root / "curriculum/modules.json").is_file() or not (root / "guides/first-semester.md").is_file():
        raise ValueError("--root must be the roadmap checkout, with its manifest and semester plan")
    source = root / "resources/tutor"
    skill = home / ".agents/skills/roadmap-tutor"
    native_skill = config / "skills/roadmap-tutor"
    agent = config / "agents/roadmap-tutor.md"
    payloads = [(destination / name, (source / "roadmap-tutor" / name).read_bytes(), boundary)
                for destination, boundary in ((skill, home), (native_skill, config))
                for name in SKILL_FILES]
    binding = (json.dumps({"roadmap_root": str(root)}, indent=2) + "\n").encode("utf-8")
    payloads += [(skill / "local.json", binding, home),
                 (native_skill / "local.json", binding, config),
                 (agent, (source / "opencode-agent.md").read_bytes(), config)]
    pending = []
    # Preflight every destination before changing any file.
    for target, data, boundary in payloads:
        check_destination(target, boundary)
        before = target.read_bytes() if target.exists() else None
        if before == data:
            continue
        if before is not None and not update:
            raise ValueError(f"Existing file differs: {target}. Review it, then use --update to back up and replace")
        pending.append((target, data, before))
    backup = None
    changed = [entry for entry in pending if entry[2] is not None]
    if changed:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
        backup = home / ".agents/tutor-backups" / stamp
        for index, (target, _, before) in enumerate(changed):
            destination = backup / f"{index}-{target.name}"
            check_destination(destination, home)
            write_atomic(destination, before)
        index_path = backup / "index.json"
        check_destination(index_path, home)
        write_atomic(index_path, json.dumps([str(entry[0]) for entry in changed], indent=2).encode("utf-8"))
    for target, data, _ in pending:
        write_atomic(target, data)
    return {"skill": str(skill), "opencode_skill": str(native_skill), "opencode_agent": str(agent), "roadmap_root": str(root),
            "written_files": len(pending), "backup": str(backup) if backup else None,
            "note": "No study records, provider settings or permissions were changed. Open a fresh session for discovery."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Roadmap checkout (defaults to this script's repository)")
    parser.add_argument("--home", type=Path, default=Path.home(), help="User home; override for an isolated installation test")
    parser.add_argument("--opencode-dir", type=Path, help="Explicit OpenCode config directory if customized")
    parser.add_argument("--update", action="store_true", help="Back up and replace changed tutor files only")
    args = parser.parse_args()
    try:
        print(json.dumps(install(args.root, args.home, update=args.update, opencode_dir=args.opencode_dir), indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"install_tutor: {exc}\n")


if __name__ == "__main__":
    main()
