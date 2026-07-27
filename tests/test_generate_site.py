import os
from pathlib import Path

from tools import generate_site


def test_extract_metadata_reads_json_block(tmp_path: Path) -> None:
    md = tmp_path / "doc.md"
    md.write_text(
        "# Title\n\n```json\n{\"id\": \"a\", \"name\": \"Aria\"}\n```\n",
        encoding="utf-8",
    )
    assert generate_site.extract_metadata(str(md)) == {"id": "a", "name": "Aria"}


def test_extract_metadata_returns_none_without_block(tmp_path: Path) -> None:
    md = tmp_path / "doc.md"
    md.write_text("# Title\n\nNo metadata here.\n", encoding="utf-8")
    assert generate_site.extract_metadata(str(md)) is None


def test_extract_metadata_returns_none_for_invalid_json(tmp_path: Path) -> None:
    md = tmp_path / "doc.md"
    md.write_text("```json\n{not valid}\n```\n", encoding="utf-8")
    assert generate_site.extract_metadata(str(md)) is None


def test_character_links_md_sorts_by_name_and_skips_index() -> None:
    metadata = {
        os.path.join("characters", "zola.md"): {"name": "Zola"},
        os.path.join("characters", "aria.md"): {"name": "Aria"},
        os.path.join("characters", "index.md"): {"name": "Index"},
        os.path.join("characters", "noname.md"): {},
        os.path.join("locations", "hub.md"): {"name": "Hub"},
    }
    result = generate_site.character_links_md(metadata)
    assert result == (
        "- [Aria](characters/aria.md)\n"
        "- [Zola](characters/zola.md)"
    )


def test_convert_links_rewrites_md_to_html() -> None:
    html = '<a href="characters/aria.md">Aria</a>'
    assert generate_site.convert_links(html) == '<a href="characters/aria.html">Aria</a>'


def test_relative_prefix_counts_directory_depth() -> None:
    assert generate_site.relative_prefix("index.html") == ""
    assert generate_site.relative_prefix(os.path.join("characters", "aria.html")) == "../"
    assert (
        generate_site.relative_prefix(os.path.join("a", "b", "c.html")) == "../../"
    )


def test_convert_file_writes_templated_html(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    md = tmp_path / "my-page.md"
    md.write_text("# Hello\n\nSee [link](other.md).\n", encoding="utf-8")
    generate_site.convert_file(str(md), os.path.join("site", "my-page.html"))

    content = (tmp_path / "site" / "my-page.html").read_text(encoding="utf-8")
    assert "<title>My Page</title>" in content
    assert "<h1>Hello</h1>" in content
    assert 'href="other.html"' in content
    assert "href='styles.css'" in content


def test_convert_file_prefix_reflects_nested_output(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    md = tmp_path / "page.md"
    md.write_text("# Nested\n", encoding="utf-8")
    generate_site.convert_file(str(md), os.path.join("site", "a", "b", "page.html"))

    content = (tmp_path / "site" / "a" / "b" / "page.html").read_text(encoding="utf-8")
    assert "href='../../styles.css'" in content
    assert "href='../../index.html'" in content


def test_convert_character_index_injects_generated_links(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    md = tmp_path / "index.md"
    md.write_text(
        "# Characters\n\n### Character Links\n\n- [Old](characters/old.md)\n",
        encoding="utf-8",
    )
    out = os.path.join("site", "characters", "index.html")
    metadata = {os.path.join("characters", "aria.md"): {"name": "Aria"}}

    generate_site.convert_character_index(str(md), out, metadata)

    content = (tmp_path / "site" / "characters" / "index.html").read_text(encoding="utf-8")
    assert "<title>Character Index</title>" in content
    assert 'href="characters/aria.html"' in content
    assert "old.html" not in content


def test_main_generates_site_from_repo(tmp_path: Path, monkeypatch) -> None:
    (tmp_path / "characters").mkdir()
    (tmp_path / "index.md").write_text("# Home\n", encoding="utf-8")
    (tmp_path / "characters" / "aria.md").write_text(
        "# Aria\n\n```json\n{\"name\": \"Aria\"}\n```\n",
        encoding="utf-8",
    )
    (tmp_path / "characters" / "index.md").write_text(
        "# Characters\n\n### Character Links\n\n- [placeholder](characters/x.md)\n",
        encoding="utf-8",
    )

    monkeypatch.chdir(tmp_path)
    generate_site.main()

    site = tmp_path / "site"
    assert (site / "index.html").is_file()
    assert (site / "characters" / "aria.html").is_file()
    assert (site / "styles.css").read_text(encoding="utf-8") == generate_site.DEFAULT_CSS
    index_html = (site / "characters" / "index.html").read_text(encoding="utf-8")
    assert 'href="characters/aria.html"' in index_html
