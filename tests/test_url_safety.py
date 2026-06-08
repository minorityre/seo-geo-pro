import socket

import pytest

from scripts import seo_url_safety


@pytest.mark.parametrize(
    "url",
    [
        "https://example.com",
        "http://example.com/path?q=1",
        "https://subdomain.example.com",
    ],
)
def test_validate_url_accepts_public_names(url):
    assert seo_url_safety.validate_url(url)


@pytest.mark.parametrize(
    "url",
    [
        "ftp://example.com",
        "file:///etc/passwd",
        "javascript:alert(1)",
        "https://localhost",
        "https://127.0.0.1",
        "http://2130706433",
        "https://metadata.google.internal.",
        "https://169.254.169.254/latest/meta-data/",
    ],
)
def test_validate_url_rejects_unsafe_targets(url):
    assert not seo_url_safety.validate_url(url)


def test_validate_url_strict_rejects_dns_to_private(monkeypatch):
    def fake_getaddrinfo(*args, **kwargs):
        return [(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", ("127.0.0.1", 443))]

    monkeypatch.setattr(socket, "getaddrinfo", fake_getaddrinfo)
    with pytest.raises(seo_url_safety.URLSafetyError):
        seo_url_safety.validate_url_strict("https://example.com")
