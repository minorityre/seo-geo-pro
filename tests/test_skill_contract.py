import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_skill_stays_compact_and_all_direct_references_exist() -> None:
    skill = read("SKILL.md")

    assert len(skill.splitlines()) < 500

    reference_links = set(re.findall(r"\]\((references/[^)#]+\.md)\)", skill))
    assert reference_links
    assert not [link for link in reference_links if not (ROOT / link).is_file()]


def test_content_depth_contract_cannot_regress_to_word_count() -> None:
    skill = read("SKILL.md")
    content_system = read("references/content-system.md")
    qa_gates = read("references/qa-gates.md")

    assert "There is no universal ideal page length" in skill
    assert "Page Admission Gate" in content_system
    assert "Depth and Completeness Gate" in content_system
    assert "Reverse outline" in content_system
    assert "Second-search test" in content_system
    assert "copy-complete" in content_system
    assert "publish-ready" in content_system
    assert "Every material number, range, threshold" in content_system
    assert "Semantic Depth and Editorial Quality" in qa_gates
    assert "Do not use word count as the acceptance test" in qa_gates


def test_growth_programmatic_and_current_geo_routes_are_present() -> None:
    skill = read("SKILL.md")
    source_of_truth = read("references/source-of-truth.md")
    programmatic = read("references/programmatic-seo.md")

    assert "references/organic-growth.md" in skill
    assert "references/programmatic-seo.md" in skill
    assert "gen-ai-performance-reports" in source_of_truth
    assert "Bing AI Performance" in source_of_truth
    assert "OAI-SearchBot" in source_of_truth
    assert "index_if" in programmatic
    assert "Stop or roll back" in programmatic


def test_agent_metadata_invokes_the_skill_explicitly() -> None:
    metadata = read("agents/openai.yaml")
    short_description = re.search(r'short_description: "([^"]+)"', metadata)

    assert short_description
    assert 25 <= len(short_description.group(1)) <= 64
    assert "$seo-geo-pro" in metadata
