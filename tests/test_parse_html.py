from scripts.seo_parse_html import parse_html


def test_parse_html_extracts_core_seo_fields():
    html = """
    <html>
      <head>
        <title>Example Title</title>
        <meta name="description" content="Useful description">
        <meta name="robots" content="index,follow">
        <link rel="canonical" href="/canonical">
        <script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"Example"}</script>
      </head>
      <body>
        <h1>Main Heading</h1>
        <h2>Section</h2>
        <img src="/image.jpg" alt="Descriptive alt" loading="lazy">
        <a href="/internal">Internal</a>
        <a href="https://other.example/page">External</a>
        <p>This is a useful paragraph with words for counting.</p>
      </body>
    </html>
    """

    result = parse_html(html, "https://example.com/page")

    assert result["title"] == "Example Title"
    assert result["meta_description"] == "Useful description"
    assert result["meta_robots"] == "index,follow"
    assert result["canonical"] == "https://example.com/canonical"
    assert result["h1"] == ["Main Heading"]
    assert result["h2"] == ["Section"]
    assert result["schema"][0]["@type"] == "Organization"
    assert result["images"][0]["lazy_method"] == "native"
    assert result["links"]["internal"][0]["href"] == "https://example.com/internal"
    assert result["links"]["external"][0]["href"] == "https://other.example/page"
    assert result["word_count"] > 5
