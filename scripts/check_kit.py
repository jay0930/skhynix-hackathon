"""추가 패키지 없이 준비 키트의 파일·링크·원본 무결성을 검사합니다."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

SKILLS: tuple[str, ...] = (
    "idea-partner", "hackathon-start", "tdd-delivery", "delivery-review", "ponytail",
)
TEMPLATES: tuple[str, ...] = (
    "PRD", "REQUIREMENTS", "TRD", "TASKS", "DECISIONS", "VERIFICATION",
)
REQUIRED: tuple[str, ...] = (
    "README.md", "AGENTS.md", ".gitignore", "third-party/NOTICE.md",
    "third-party/sources.json", "docs/REHEARSAL.md", "docs/TOOLING.md",
    "docs/VALIDATION.md", "scripts/check_kit.py", "scripts/test_check_kit.py",
) + tuple(f"templates/{name}.md" for name in TEMPLATES) + tuple(
    f".agents/skills/{name}/SKILL.md" for name in SKILLS
) + tuple(f"third-party/{name}/LICENSE" for name in ("ponytail", "superpowers", "gstack"))
IGNORED: frozenset[str] = frozenset({".git", "__pycache__", ".pytest_cache"})


def public_files(root: Path) -> list[Path]:
    """로컬 참고 자료·Git 내부·검사 캐시를 제외한 공개 후보를 반환합니다."""
    paths: list[Path] = []
    for path in sorted(root.rglob("*")):
        parts: tuple[str, ...] = path.relative_to(root).parts
        if parts[0] == "local" or any(part in IGNORED for part in parts):
            continue
        if path.is_symlink() or path.is_file():
            paths.append(path)
    return paths


def check_links(path: Path, text: str, root: Path) -> list[str]:
    """상대 링크가 공개 키트 안에 존재하는지 검사합니다. 원격 접속은 하지 않습니다."""
    errors: list[str] = []
    body: str = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", body):
        target: str = match.group(1).strip().strip("<>")
        parsed = urlsplit(target)
        if parsed.scheme or target.startswith("#"):
            continue
        relative: str = unquote(parsed.path)
        destination: Path = (path.parent / relative).resolve()
        try:
            inside: Path = destination.relative_to(root)
        except ValueError:
            errors.append(f"LINK PATH: {path.relative_to(root)} -> {relative}")
            continue
        if inside.parts and inside.parts[0] == "local":
            errors.append(f"PRIVATE LINK: {path.relative_to(root)} -> {relative}")
        elif not destination.exists():
            errors.append(f"BROKEN LINK: {path.relative_to(root)} -> {relative}")
    return errors


def check_sources(root: Path) -> list[str]:
    """배포 원본의 커밋·해시·보관 경계를 검사합니다."""
    errors: list[str] = []
    manifest: Path = root / "third-party/sources.json"
    try:
        entries = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, ValueError, UnicodeError):
        return ["SOURCE: third-party/sources.json is missing or invalid"]
    if not isinstance(entries, list) or not entries:
        return ["SOURCE: manifest must be a non-empty list"]
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("SOURCE: entry must be an object")
            continue
        fields: tuple[str, ...] = ("repository", "commit", "path", "url", "sha256", "local_path")
        if any(not isinstance(entry.get(key), str) or not entry[key] for key in fields):
            errors.append("SOURCE: missing string field")
            continue
        label: str = entry["repository"] + "/" + entry["path"]
        if not re.fullmatch(r"[0-9a-f]{40}", entry["commit"]):
            errors.append(f"SOURCE COMMIT: {label}")
        expected_url: str = f'https://github.com/{entry["repository"]}/blob/{entry["commit"]}/{entry["path"]}'
        if entry["url"] != expected_url:
            errors.append(f"SOURCE URL: {label}")
        if not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            errors.append(f"SOURCE HASH FORMAT: {label}")
        destination: Path = (root / entry["local_path"]).resolve()
        try:
            inside: Path = destination.relative_to(root)
        except ValueError:
            errors.append(f"SOURCE PATH: {label}")
            continue
        distributed = entry.get("redistributed")
        if not isinstance(distributed, bool):
            errors.append(f"SOURCE FLAG: {label}")
        elif distributed:
            if inside.parts and inside.parts[0] == "local":
                errors.append(f"SOURCE PRIVATE PATH: {label}")
            elif not destination.is_file():
                errors.append(f"SOURCE MISSING: {entry['local_path']}")
            elif hashlib.sha256(destination.read_bytes()).hexdigest() != entry["sha256"]:
                errors.append(f"SOURCE HASH: {entry['local_path']}")
        elif not inside.parts or inside.parts[0] != "local":
            errors.append(f"SOURCE PRIVATE PATH: {label}")
    return errors


def validate(root: Path) -> list[str]:
    """로컬 내용을 표시하지 않고 공개 후보의 구조적 문제를 반환합니다."""
    root = root.resolve()
    errors: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"MISSING: {relative}")
    for path in public_files(root):
        relative: str = path.relative_to(root).as_posix()
        if path.is_symlink():
            errors.append(f"SYMLINK: {relative}")
            continue
        if (path.suffix.lower() in {".pdf", ".zip", ".pem", ".key"}
                or path.name == ".env" or path.name.startswith(".env.") and path.name != ".env.example"):
            errors.append(f"PRIVATE FILE: {relative}")
            continue
        if path.suffix not in {".md", ".json"}:
            continue
        try:
            text: str = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append(f"UNREADABLE: {relative}")
            continue
        if re.search(r"/(?:Users|home)/[^\s\"<>]+", text):
            errors.append(f"PRIVATE ABSOLUTE PATH: {relative}")
        if path.suffix == ".md":
            errors.extend(check_links(path, text, root))
        if path.name == "SKILL.md":
            front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
            if front is None:
                errors.append(f"SKILL FRONTMATTER: {relative}")
            else:
                name = re.search(r"^name: ([a-z0-9-]+)$", front.group(1), re.MULTILINE)
                if name is None or name.group(1) != path.parent.name:
                    errors.append(f"SKILL NAME: {relative}")
                if not re.search(r"^description: \S", front.group(1), re.MULTILINE):
                    errors.append(f"SKILL DESCRIPTION: {relative}")
    agents: Path = root / "AGENTS.md"
    if agents.is_file() and len(agents.read_text(encoding="utf-8").splitlines()) > 200:
        errors.append("SIZE: AGENTS.md exceeds 200 lines")
    errors.extend(check_sources(root))
    return errors


def main() -> int:
    """검사 결과만 출력하고 오류가 있으면 실패 코드로 종료합니다."""
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args: argparse.Namespace = parser.parse_args()
    try:
        errors: list[str] = validate(args.root)
    except (OSError, ValueError) as error:
        print(f"검사 실행 실패: {type(error).__name__}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("준비 키트 검사 통과: 필수 파일·상대 링크·Skill 메타데이터·배포 원본 해시")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
