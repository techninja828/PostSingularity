from pathlib import Path

from tools import markdown_utils
from tools.scripts import check_cohesion, validate_metadata


def test_markdown_collectors_skip_generated_and_vcs_directories(
    tmp_path: Path,
) -> None:
    visible = tmp_path / "content.md"
    visible.write_text("# Content\n", encoding="utf-8")

    excluded_paths = [
        tmp_path / ".git" / "logs" / "remote.md",
        tmp_path / ".venv" / "package.md",
        tmp_path / "node_modules" / "dependency.md",
    ]
    for path in excluded_paths:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("not repository content", encoding="utf-8")

    expected = {str(visible)}
    assert set(validate_metadata.collect_markdown_files(str(tmp_path))) == expected
    assert set(check_cohesion.collect_markdown_files(str(tmp_path))) == expected


def test_shared_markdown_parsers_extract_tags_and_json_blocks() -> None:
    text = (
        "# Title\n"
        "Tags: [AI], [Governance]\n\n"
        "## Section\n\n"
        "```json\n{\"id\": \"one\"}\n```\n\n"
        "```json\n{ broken }\n```\n\n"
        "```json\n{\"id\": \"two\"}\n```\n"
    )

    assert markdown_utils.parse_tags(text) == ("ai", "governance")
    assert markdown_utils.extract_title(text, "fallback") == "Title"
    assert markdown_utils.extract_headings(text) == ("Title", "Section")
    assert markdown_utils.has_tag_line(text) and markdown_utils.has_json_block(text)
    assert markdown_utils.extract_json_blocks(text) == [{"id": "one"}, {"id": "two"}]
    assert markdown_utils.first_json_block(text) == {"id": "one"}


def test_read_text_returns_none_for_missing_file(tmp_path: Path) -> None:
    assert markdown_utils.read_text(str(tmp_path / "absent.md")) is None
