#!/usr/bin/env python3
"""Scan public copy for internal SEO strategy language before publishing."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

try:
    from .seo_url_safety import safe_requests_get
except ImportError:  # pragma: no cover - CLI execution
    from seo_url_safety import safe_requests_get


DEFAULT_PATTERNS = [
    r"\bseo\s+ownership\b",
    r"\bownership\s+seo\b",
    r"\bowner(?:s)?\b",
    r"\bcannibali[sz]\w*\b",
    r"\bgeneric\s+landing\b",
    r"\bdifferent\s+intent\b",
    r"\bbriefing\b",
    r"\bseo\s+hypothesis\b",
    r"\bquick\s+win(?:s)?\b",
    r"\bthin\s+content\b",
    r"\bmoney\s+page\b",
    r"\bserp\s+ownership\b",
    r"\bcrawl\s+budget\b",
    r"\binternal\s+seo\s+note\b",
    r"\bcluster\s+ownership\b",
]

TEXT_EXTENSIONS = {
    ".html",
    ".htm",
    ".txt",
    ".md",
    ".mdx",
    ".tsx",
    ".ts",
    ".jsx",
    ".js",
    ".json",
    ".liquid",
    ".vue",
    ".astro",
}

SKIP_DIRS = {".git", ".next", "node_modules", "dist", "build", "coverage", ".vercel", ".turbo", "__pycache__"}


def is_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://")


def normalize_text(value: str) -> str:
    value = re.sub(r"<script[\s\S]*?</script>", " ", value, flags=re.I)
    value = re.sub(r"<style[\s\S]*?</style>", " ", value, flags=re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    return re.sub(r"\s+", " ", value)


def read_file(path: Path) -> str:
    raw = path.read_bytes()
    for encoding in ("utf-8", "utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def fetch_url(url: str, timeout: int) -> str:
    response = safe_requests_get(
        url,
        timeout=timeout,
        headers={"User-Agent": "SEO-GEO-Pro-public-copy-guard/1.0", "Accept": "text/html,text/plain,*/*"},
    )
    return response.text


def iter_files(path: Path):
    if path.is_file():
        if path.suffix.lower() in TEXT_EXTENSIONS:
            yield path
        return
    for child in path.rglob("*"):
        if any(part in SKIP_DIRS for part in child.parts):
            continue
        if child.is_file() and child.suffix.lower() in TEXT_EXTENSIONS:
            yield child


def scan_text(label: str, text: str, patterns: list[re.Pattern[str]]):
    normalized = normalize_text(text)
    findings = []
    for pattern in patterns:
        for match in pattern.finditer(normalized):
            start = max(0, match.start() - 70)
            end = min(len(normalized), match.end() + 70)
            findings.append({"target": label, "pattern": pattern.pattern, "context": normalized[start:end].strip()})
    return findings


def run(targets: list[str], timeout: int = 20, extra_patterns: list[str] | None = None) -> tuple[list[dict], list[str]]:
    compiled = [re.compile(pattern, flags=re.I | re.U) for pattern in [*DEFAULT_PATTERNS, *(extra_patterns or [])]]
    findings: list[dict] = []
    errors: list[str] = []
    for target in targets:
        if is_url(target):
            try:
                findings.extend(scan_text(target, fetch_url(target, timeout), compiled))
            except Exception as exc:
                errors.append(f"{target}: {exc}")
            continue

        path = Path(target)
        if not path.exists():
            errors.append(f"{target}: path does not exist")
            continue
        for file_path in iter_files(path):
            try:
                findings.extend(scan_text(str(file_path), read_file(file_path), compiled))
            except Exception as exc:
                errors.append(f"{file_path}: {exc}")
    return findings, errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan public copy for internal SEO language.")
    parser.add_argument("targets", nargs="+", help="Files, directories or URLs.")
    parser.add_argument("--timeout", type=int, default=20)
    parser.add_argument("--pattern", action="append", default=[], help="Additional regex to flag.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    findings, errors = run(args.targets, timeout=args.timeout, extra_patterns=args.pattern)
    if args.json:
        import json

        print(json.dumps({"findings": findings, "errors": errors}, indent=2))
    else:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        if findings:
            print("Public copy guard failed. Internal SEO language found:\n")
            for item in findings:
                print(f"- {item['target']}")
                print(f"  pattern: {item['pattern']}")
                print(f"  context: {item['context']}\n")
        else:
            print("Public copy guard passed. No internal SEO language found.")

    if findings:
        return 1
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
