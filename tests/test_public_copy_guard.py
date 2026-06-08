from pathlib import Path

from scripts.seo_public_copy_guard import run


def test_public_copy_guard_passes_clean_copy(tmp_path: Path):
    page = tmp_path / "page.html"
    page.write_text("<h1>Organic growth for ecommerce teams</h1><p>Clear strategy and practical execution.</p>", encoding="utf-8")

    findings, errors = run([str(page)])

    assert findings == []
    assert errors == []


def test_public_copy_guard_flags_internal_language(tmp_path: Path):
    page = tmp_path / "page.html"
    page.write_text("<p>This is a quick win for the money page.</p>", encoding="utf-8")

    findings, errors = run([str(page)])

    assert errors == []
    assert len(findings) == 2
