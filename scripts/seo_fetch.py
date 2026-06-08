#!/usr/bin/env python3
"""Safely fetch a public URL for SEO inspection."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from .seo_url_safety import URLSafetyError, safe_requests_get
except ImportError:  # pragma: no cover - CLI execution
    from seo_url_safety import URLSafetyError, safe_requests_get


USER_AGENT = "SEO-GEO-Pro/1.0 (+https://github.com/minorityre/seo-geo-pro)"


def fetch(url: str, timeout: int = 30) -> dict:
    response = safe_requests_get(
        url,
        timeout=timeout,
        allow_redirects=True,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,text/plain,*/*",
        },
    )
    return {
        "url": url,
        "final_url": response.url,
        "status_code": response.status_code,
        "content_type": response.headers.get("content-type"),
        "headers": dict(response.headers),
        "redirect_chain": [{"url": item.url, "status_code": item.status_code} for item in response.history],
        "text": response.text,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch a URL with SSRF-safe validation.")
    parser.add_argument("url")
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--json", action="store_true", help="Print a JSON summary with truncated text.")
    parser.add_argument("--output", "-o", help="Write full response text to a file.")
    args = parser.parse_args()

    try:
        result = fetch(args.url, timeout=args.timeout)
    except (URLSafetyError, Exception) as exc:
        print(f"fetch failed: {exc}", file=sys.stderr)
        return 1

    if args.output:
        Path(args.output).write_text(result["text"], encoding="utf-8")

    if args.json:
        summary = dict(result)
        text = summary.get("text") or ""
        summary["text"] = text[:1000] + ("..." if len(text) > 1000 else "")
        print(json.dumps(summary, indent=2))
    elif not args.output:
        print(result["text"])
    else:
        print(f"saved {len(result['text'])} characters from {result['final_url']} to {args.output}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
