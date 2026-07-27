from datetime import date, timedelta
from pathlib import Path

from tools import research_agent as agent


def test_slugify_and_tag_parsing() -> None:
    assert agent.slugify("Brain Chemistry Control!") == "brain-chemistry-control"
    assert agent.parse_tags("# Test\nTags: [AI], [Governance]\n") == (
        "ai",
        "governance",
    )


def test_assumption_registry_is_valid_and_points_to_canon() -> None:
    assumptions = agent.load_assumptions()
    assert len(assumptions) >= 10
    assert len({item["id"] for item in assumptions}) == len(assumptions)
    for item in assumptions:
        for canon_path in item["canon_sources"]:
            assert (agent.REPO_ROOT / canon_path).is_file(), (
                f"{item['id']} references missing canon {canon_path}"
            )


def test_lane_inference_and_assumption_selection() -> None:
    assumptions = agent.load_assumptions()
    topic = "humanoid robot dexterity and autonomous warehouse logistics"
    lane = agent.infer_lane(topic, assumptions)
    selected = agent.select_assumptions(topic, lane, assumptions)
    assert lane == "robotics"
    assert selected[0]["id"] == "PS-ROBOTICS-001"


def test_nearby_canon_explains_why_files_match() -> None:
    documents = agent.load_canon_files()
    matches = agent.nearby_canon(
        "personal AI agents with persistent memory and consent",
        "ai",
        documents,
    )
    assert matches
    assert any(match.path.endswith("ai-agents.md") for match in matches)
    assert all(match.reason for match in matches)
    assert all(match.headings for match in matches)


def test_canon_context_guarantees_declared_assumption_sources() -> None:
    assumptions = agent.load_assumptions()
    selected = agent.select_assumptions(
        "automation, future of work, meaning, and social adaptation",
        "social-systems",
        assumptions,
    )
    matches = agent.select_canon_context(
        "automation, future of work, meaning, and social adaptation",
        "social-systems",
        agent.load_canon_files(),
        selected,
    )

    declared_paths = {
        path for assumption in selected for path in assumption["canon_sources"]
    }
    matched_paths = {match.path for match in matches}
    assert declared_paths <= matched_paths
    assert all(match.headings for match in matches)
    assert all(match.excerpt for match in matches)
    assert any(match.assumption_ids for match in matches)


def test_mock_brief_formats_as_metadata_valid_markdown() -> None:
    assumptions = agent.load_assumptions()
    topic = "AI agent memory and consent"
    selected = agent.select_assumptions(topic, "ai", assumptions)
    matches = agent.select_canon_context(
        topic,
        "ai",
        agent.load_canon_files(),
        selected,
    )
    brief = agent.build_mock_brief(
        topic,
        "ai",
        selected,
        matches,
        date(2026, 7, 26),
        30,
    )
    markdown = agent.format_memo(
        brief,
        topic,
        selected,
        matches,
        date(2026, 7, 26),
        "gpt-5.6",
        mock=True,
    )
    assert "MOCK - synthetic test data" in markdown
    assert "PS-AI-002" in markdown
    assert "## Canon Implementation Plan" in markdown
    assert "Proposed change:" in markdown
    assert "Implementation steps:" in markdown
    assert agent.parse_tags(markdown)
    assert "```json" in markdown

    brief.canon_implications[0].target_heading = "Invented heading"
    try:
        agent.validate_brief(brief, selected, matches)
    except ValueError as exc:
        assert "Unknown target heading" in str(exc)
    else:
        raise AssertionError("Invented repository headings must be rejected")


def test_write_memo_avoids_overwrite(tmp_path: Path) -> None:
    first = agent.write_memo("one", "Agent memory", "ai", tmp_path, date(2026, 7, 26))
    second = agent.write_memo("two", "Agent memory", "ai", tmp_path, date(2026, 7, 26))
    assert first.name == "2026-07-26-ai-agent-memory.md"
    assert second.name == "2026-07-26-ai-agent-memory-2.md"
    assert first.read_text(encoding="utf-8") == "one"
    assert second.read_text(encoding="utf-8") == "two"


def test_append_submission_log_is_idempotent(tmp_path: Path) -> None:
    report = tmp_path / "pending-review" / "agent-research" / "brief.md"
    report.parent.mkdir(parents=True)
    report.write_text("brief", encoding="utf-8")
    log = tmp_path / "submissions-log.md"
    log.write_text(
        "| Cycle | Contributor | File/Idea | Status | Notes |\n"
        "|---|---|---|---|---|\n"
        "\nPlease append new rows when submitting.\n",
        encoding="utf-8",
    )
    assert agent.append_submission_log(log, report, "test topic", tmp_path)
    assert not agent.append_submission_log(log, report, "test topic", tmp_path)
    text = log.read_text(encoding="utf-8")
    assert text.count("brief.md") == 2


def test_append_submission_log_row_joins_table(tmp_path: Path) -> None:
    report = tmp_path / "pending-review" / "agent-research" / "brief.md"
    report.parent.mkdir(parents=True)
    report.write_text("brief", encoding="utf-8")
    log = tmp_path / "submissions-log.md"
    log.write_text(
        "| Cycle | Contributor | File/Idea | Status | Notes |\n"
        "|---|---|---|---|---|\n"
        "| 0 | repo setup | pending-review folder | accepted | initial structure |\n"
        "\nPlease append new rows when submitting.\n",
        encoding="utf-8",
    )
    assert agent.append_submission_log(log, report, "test topic", tmp_path)
    lines = log.read_text(encoding="utf-8").splitlines()
    table_indices = [i for i, line in enumerate(lines) if line.startswith("|")]
    # Every table row must be contiguous so the new entry renders inside the table.
    assert table_indices == list(range(table_indices[0], table_indices[-1] + 1))
    assert lines[table_indices[-1]].startswith("| 0 | research agent |")


def test_scheduled_topic_is_deterministic() -> None:
    first = agent.scheduled_topic(date(2026, 7, 26))
    second = agent.scheduled_topic(date(2026, 7, 26))
    assert first == second
    assert first[0] in agent.LANES


def test_daily_rotation_cycles_every_lane() -> None:
    lane_count = len(agent.LANES)
    lanes = [
        agent.scheduled_topic(date(2026, 7, 26) + timedelta(days=offset))[0]
        for offset in range(lane_count)
    ]
    # Consecutive days must differ and a full period must cover every lane.
    assert lanes[0] != lanes[1]
    assert set(lanes) == set(agent.LANES)
