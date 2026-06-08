#!/usr/bin/env python3
"""Render JavaScript pages for SEO inspection with Playwright when available."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from .seo_fetch import fetch
    from .seo_url_safety import URLSafetyError, validate_url_strict
except ImportError:  # pragma: no cover - CLI execution
    from seo_fetch import fetch
    from seo_url_safety import URLSafetyError, validate_url_strict

try:
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover - optional dependency
    sync_playwright = None


SPA_MARKERS = (
    '<div id="root"></div>',
    '<div id="__next">',
    '<div id="app"></div>',
    '<div id="__nuxt">',
    "<astro-island",
    "you need to enable javascript",
    "please enable javascript",
)


def looks_like_spa(html: str | None) -> bool:
    if not html:
        return True
    lower = html.lower()
    return any(marker in lower for marker in SPA_MARKERS)


def render_page(url: str, mode: str = "auto", timeout_ms: int = 15000) -> dict:
    if mode not in {"auto", "always", "never"}:
        return {"url": url, "error": f"invalid mode: {mode}"}

    try:
        validate_url_strict(url)
        raw = fetch(url)
    except Exception as exc:
        return {"url": url, "error": f"raw fetch failed: {exc}"}

    is_spa = looks_like_spa(raw["text"])
    should_render = mode == "always" or (mode == "auto" and is_spa)
    result = {
        "url": url,
        "final_url": raw["final_url"],
        "status_code": raw["status_code"],
        "mode_used": "raw",
        "is_spa": is_spa,
        "raw_html": raw["text"],
        "html": raw["text"],
        "console_errors": [],
        "error": None,
    }

    if not should_render or mode == "never":
        return result

    if sync_playwright is None:
        result["error"] = "playwright is required for rendered mode. Install with: pip install -r requirements.txt && playwright install chromium"
        return result

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": 1366, "height": 768},
                user_agent="SEO-GEO-Pro/1.0",
            )
            page = context.new_page()
            page.route("**/*", _safe_route)
            page.on("console", lambda msg: result["console_errors"].append(msg.text) if msg.type == "error" else None)
            response = page.goto(url, wait_until="networkidle", timeout=timeout_ms)
            page.wait_for_timeout(500)
            result.update(
                {
                    "final_url": page.url,
                    "status_code": response.status if response else raw["status_code"],
                    "mode_used": "rendered",
                    "html": page.content(),
                }
            )
            browser.close()
    except Exception as exc:
        result["error"] = f"render failed: {exc}"
    return result


def _safe_route(route, request):  # type: ignore[no-untyped-def]
    """Fail closed on subresource requests to private or unsupported targets."""
    try:
        if request.url.startswith(("data:", "blob:", "about:")):
            route.continue_()
            return
        validate_url_strict(request.url)
        route.continue_()
    except Exception:
        route.abort()


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a URL for SEO inspection.")
    parser.add_argument("url")
    parser.add_argument("--mode", choices=("auto", "always", "never"), default="auto")
    parser.add_argument("--timeout-ms", type=int, default=15000)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output", "-o")
    args = parser.parse_args()

    result = render_page(args.url, mode=args.mode, timeout_ms=args.timeout_ms)
    if args.output and result.get("html"):
        Path(args.output).write_text(result["html"], encoding="utf-8")

    if args.json:
        summary = dict(result)
        for key in ("html", "raw_html"):
            value = summary.get(key) or ""
            summary[key] = value[:1000] + ("..." if len(value) > 1000 else "")
        print(json.dumps(summary, indent=2))
    elif result.get("html"):
        print(result["html"])
    else:
        print(result.get("error") or "no HTML returned", file=sys.stderr)

    return 1 if result.get("error") else 0


if __name__ == "__main__":
    raise SystemExit(main())
