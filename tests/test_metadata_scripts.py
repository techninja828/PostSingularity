from pathlib import Path

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
