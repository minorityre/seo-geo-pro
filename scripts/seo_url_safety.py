#!/usr/bin/env python3
"""URL safety helpers for SEO/GEO Pro scripts.

The helpers block common SSRF targets before any network request:
loopback/private IPs, cloud metadata hosts, unsupported schemes and
obfuscated IPv4 forms such as http://2130706433/.
"""

from __future__ import annotations

import argparse
import ipaddress
import json
import re
import socket
import sys
import threading
from contextlib import contextmanager
from urllib.parse import urlparse

try:
    import requests
except ImportError as exc:  # pragma: no cover - dependency check
    raise RuntimeError("Install dependencies with: pip install -r requirements.txt") from exc


class URLSafetyError(ValueError):
    """Raised when a URL fails safety validation."""


_IPV4_OBFUSCATED_RE = re.compile(
    r"^(?:0x[0-9a-f]+|[0-9]+)(?:\.(?:0x[0-9a-f]+|[0-9]+)){0,3}$",
    re.IGNORECASE,
)

_BLOCKED_HOSTNAMES = {
    "localhost",
    "ip6-localhost",
    "ip6-loopback",
    "metadata",
    "metadata.google.internal",
    "metadata.goog",
    "metadata.azure.com",
    "metadata.ec2.internal",
    "metadata.oraclecloud.com",
    "127.0.0.1",
    "0.0.0.0",
    "::1",
    "169.254.169.254",
    "fd00:ec2::254",
}

_dns_patch_lock = threading.Lock()


def is_safe_ip(value: str) -> bool:
    """Return True when value is a public unicast IP address."""
    try:
        ip = ipaddress.ip_address(value)
    except ValueError:
        return False
    return not (
        ip.is_private
        or ip.is_loopback
        or ip.is_reserved
        or ip.is_link_local
        or ip.is_multicast
        or ip.is_unspecified
    )


def normalize_hostname(hostname: str) -> str:
    """Lowercase, strip one trailing dot and canonicalize obfuscated IPv4."""
    if not hostname:
        raise URLSafetyError("empty hostname")

    value = hostname.lower().strip()
    if value.endswith(".") and not value.endswith(".."):
        value = value[:-1]

    if _IPV4_OBFUSCATED_RE.match(value):
        try:
            value = socket.inet_ntoa(socket.inet_aton(value))
        except OSError as exc:
            raise URLSafetyError(f"malformed IPv4 hostname: {hostname}") from exc
    return value


def validate_url(url: str) -> bool:
    """Parse-only validation for quick checks. Does not resolve DNS."""
    try:
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            return False
        host = normalize_hostname(parsed.hostname)
        if host in _BLOCKED_HOSTNAMES:
            return False
        try:
            ipaddress.ip_address(host)
        except ValueError:
            return True
        return is_safe_ip(host)
    except Exception:
        return False


def validate_url_strict(url: str) -> tuple[str, str]:
    """Validate URL and resolve hostname to a public IP.

    Returns (url, pinned_ipv4). Every returned A record must be public.
    """
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise URLSafetyError(f"invalid scheme: {parsed.scheme!r}")
    if not parsed.hostname:
        raise URLSafetyError("missing hostname")

    host = normalize_hostname(parsed.hostname)
    if host in _BLOCKED_HOSTNAMES:
        raise URLSafetyError(f"blocked hostname: {host}")

    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        ip = None

    if ip is not None:
        if not is_safe_ip(host):
            raise URLSafetyError(f"blocked IP literal: {host}")
        return url, str(ip)

    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    try:
        addrinfo = socket.getaddrinfo(host, port, family=socket.AF_INET, type=socket.SOCK_STREAM)
    except socket.gaierror as exc:
        raise URLSafetyError(f"DNS resolution failed for {host}: {exc}") from exc

    resolved = sorted({item[4][0] for item in addrinfo})
    if not resolved:
        raise URLSafetyError(f"no A records for {host}")
    for ip_value in resolved:
        if not is_safe_ip(ip_value):
            raise URLSafetyError(f"refused non-public DNS result: {host} -> {ip_value}")
    return url, resolved[0]


@contextmanager
def _pin_dns(hostname: str, pinned_ip: str, port: int):
    """Temporarily pin a hostname to a pre-validated IP for requests."""
    if not _dns_patch_lock.acquire(blocking=False):
        raise URLSafetyError("DNS-pinned fetch already in progress")

    original_getaddrinfo = socket.getaddrinfo
    target = hostname.lower()

    def patched(host, requested_port, *args, **kwargs):
        if host and str(host).lower() == target:
            family = kwargs.get("family", args[0] if args else 0)
            if family in (0, socket.AF_UNSPEC, socket.AF_INET):
                return [
                    (
                        socket.AF_INET,
                        socket.SOCK_STREAM,
                        socket.IPPROTO_TCP,
                        "",
                        (pinned_ip, requested_port or port),
                    )
                ]
            raise socket.gaierror(socket.EAI_FAIL, "address family refused for pinned host")

        result = original_getaddrinfo(host, requested_port, *args, **kwargs)
        for item in result:
            ip_value = item[4][0]
            if not is_safe_ip(ip_value):
                raise socket.gaierror(socket.EAI_FAIL, f"refused non-public IP {ip_value}")
        return result

    socket.getaddrinfo = patched  # type: ignore[assignment]
    try:
        yield
    finally:
        socket.getaddrinfo = original_getaddrinfo  # type: ignore[assignment]
        _dns_patch_lock.release()


def safe_requests_get(url: str, *, timeout: int = 30, **kwargs):
    """Run requests.get with strict URL validation and DNS pinning."""
    normalized_url, pinned_ip = validate_url_strict(url)
    parsed = urlparse(normalized_url)
    assert parsed.hostname is not None
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    with _pin_dns(parsed.hostname, pinned_ip, port):
        return requests.get(normalized_url, timeout=timeout, **kwargs)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a URL against SEO/GEO Pro safety rules.")
    parser.add_argument("url")
    parser.add_argument("--strict", action="store_true", help="Resolve DNS and block non-public targets.")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    result: dict[str, object] = {"url": args.url, "ok": False, "mode": "strict" if args.strict else "parse"}
    try:
        if args.strict:
            _, pinned_ip = validate_url_strict(args.url)
            result.update({"ok": True, "pinned_ip": pinned_ip})
        else:
            result["ok"] = validate_url(args.url)
    except URLSafetyError as exc:
        result["error"] = str(exc)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("OK" if result["ok"] else f"BLOCKED: {result.get('error', 'parse-time rejection')}")
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
