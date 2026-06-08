#!/usr/bin/env python3
"""Parse HTML and extract SEO-relevant elements."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

try:
    from bs4 import BeautifulSoup
except ImportError as exc:  # pragma: no cover - dependency check
    raise RuntimeError("Install dependencies with: pip install -r requirements.txt") from exc


def _text(node) -> str:
    return node.get_text(" ", strip=True) if node else ""


def _lazy_method(img) -> str:
    classes = set(img.get("class") or [])
    attrs = img.attrs
    if str(img.get("loading", "")).lower() == "lazy":
        return "native"
    if attrs.get("data-perfmatters-src") or "perfmatters-lazy" in classes:
        return "perfmatters"
    if attrs.get("data-ewww-src") or "lazyload-eio" in classes:
        return "ewww"
    if any(attrs.get(name) for name in ("data-src", "data-lazy-src", "data-original", "data-srcset")):
        return "js-generic"
    if classes & {"lazy", "lazyload", "lazyloaded", "lazy-loaded"}:
        return "js-generic"
    return "none"


def parse_html(html: str, base_url: str | None = None) -> dict[str, Any]:
    soup = BeautifulSoup(html, "lxml" if _has_lxml() else "html.parser")
    base_domain = urlparse(base_url).netloc if base_url else ""

    result: dict[str, Any] = {
        "title": _text(soup.find("title")) or None,
        "meta_description": None,
        "meta_robots": None,
        "canonical": None,
        "h1": [],
        "h2": [],
        "h3": [],
        "hreflang": [],
        "open_graph": {},
        "twitter_card": {},
        "schema": [],
        "images": [],
        "links": {"internal": [], "external": []},
        "word_count": 0,
    }

    for meta in soup.find_all("meta"):
        name = str(meta.get("name", "")).lower()
        prop = str(meta.get("property", "")).lower()
        content = meta.get("content", "")
        if name == "description":
            result["meta_description"] = content
        elif name == "robots":
            result["meta_robots"] = content
        if prop.startswith("og:"):
            result["open_graph"][prop] = content
        if name.startswith("twitter:"):
            result["twitter_card"][name] = content

    canonical = soup.find("link", rel=lambda value: value and "canonical" in value)
    if canonical and canonical.get("href"):
        result["canonical"] = urljoin(base_url, canonical["href"]) if base_url else canonical["href"]

    for link in soup.find_all("link", rel=lambda value: value and "alternate" in value):
        if link.get("hreflang") and link.get("href"):
            result["hreflang"].append(
                {
                    "lang": link.get("hreflang"),
                    "href": urljoin(base_url, link["href"]) if base_url else link["href"],
                }
            )

    for tag in ("h1", "h2", "h3"):
        result[tag] = [_text(node) for node in soup.find_all(tag) if _text(node)]

    for script in soup.find_all("script", type="application/ld+json"):
        raw = script.string or script.get_text()
        try:
            data = json.loads(raw)
        except Exception:
            continue
        if isinstance(data, dict) and isinstance(data.get("@graph"), list):
            result["schema"].extend(item for item in data["@graph"] if isinstance(item, dict))
        elif isinstance(data, list):
            result["schema"].extend(item for item in data if isinstance(item, dict))
        else:
            result["schema"].append(data)

    for img in soup.find_all("img"):
        src = img.get("src") or ""
        result["images"].append(
            {
                "src": urljoin(base_url, src) if base_url and src else src,
                "alt": img.get("alt"),
                "width": img.get("width"),
                "height": img.get("height"),
                "loading": img.get("loading"),
                "lazy_method": _lazy_method(img),
            }
        )

    if base_url:
        for anchor in soup.find_all("a", href=True):
            href = anchor.get("href", "")
            if not href or href.startswith("#") or href.lower().startswith(("javascript:", "mailto:", "tel:")):
                continue
            absolute = urljoin(base_url, href)
            bucket = "internal" if urlparse(absolute).netloc == base_domain else "external"
            result["links"][bucket].append({"href": absolute, "text": _text(anchor)[:120], "rel": anchor.get("rel", [])})

    for node in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        node.decompose()
    words = re.findall(r"\b[\w'-]+\b", soup.get_text(" ", strip=True))
    result["word_count"] = len(words)
    return result


def _has_lxml() -> bool:
    try:
        import lxml  # noqa: F401
    except ImportError:
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Parse HTML for SEO elements.")
    parser.add_argument("file", nargs="?", help="HTML file. Reads stdin when omitted.")
    parser.add_argument("--base-url", "--url", dest="base_url")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    html = Path(args.file).read_text(encoding="utf-8") if args.file else sys.stdin.read()
    result = parse_html(html, args.base_url)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"Title: {result['title']}")
        print(f"Meta description: {result['meta_description']}")
        print(f"Canonical: {result['canonical']}")
        print(f"H1: {len(result['h1'])}")
        print(f"H2: {len(result['h2'])}")
        print(f"Images: {len(result['images'])}")
        print(f"Internal links: {len(result['links']['internal'])}")
        print(f"External links: {len(result['links']['external'])}")
        print(f"Schema blocks: {len(result['schema'])}")
        print(f"Word count: {result['word_count']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
