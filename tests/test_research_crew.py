import json
from pathlib import Path

import pytest

from tools import research_crew as crew_module
from tools.research_agent import (
    ResearchBrief,
    Source,
    load_assumptions,
    load_canon_files,
    select_assumptions,
    select_canon_context,
)


def test_crewai_model_name_adds_provider_prefix() -> None:
    assert crew_module.crewai_model_name("gpt-5.6") == "openai/gpt-5.6"
    assert crew_module.crewai_model_name("openai/gpt-5.6") == "openai/gpt-5.6"


def test_intermediate_schemas_are_strict() -> None:
    assert crew_module.EvidencePacket.model_config["extra"] == "forbid"
    assert crew_module.AuditedEvidence.model_config["extra"] == "forbid"
    assert crew_module.AnalysisPacket.model_config["extra"] == "forbid"
    assert crew_module.ImplementationPacket.model_config["extra"] == "forbid"


def test_source_urls_remain_validated_json_strings() -> None:
    source = Source(
        id="S1",
        title="Primary source",
        url="https://example.com/research",
        publisher="Example",
        published_at="2026-07-26",
        source_type="primary-research",
        why_relevant="Regression coverage for CrewAI task persistence.",
    )

    assert source.url == "https://example.com/research"
    assert json.loads(json.dumps(source.model_dump()))["url"] == source.url

    with pytest.raises(ValueError):
        Source(
            id="S2",
            title="Invalid source",
            url="not-a-url",
            publisher="Example",
            published_at="unknown",
            source_type="mock",
            why_relevant="This must fail validation.",
        )


def test_mock_crew_cli_uses_existing_pipeline(capsys) -> None:
    result = crew_module.main(
        [
            "--topic",
            "persistent AI agent memory",
            "--lane",
            "ai",
            "--mock",
            "--dry-run",
        ]
    )
    assert result == 0
    output = capsys.readouterr().out
    assert "MOCK - synthetic test data" in output
    assert "Non-canonical research draft" in output


def test_build_research_crew_has_six_bounded_roles(monkeypatch) -> None:
    monkeypatch.setenv("OPENAI_API_KEY", "test-only-not-a-real-key")
    monkeypatch.setenv("OTEL_SDK_DISABLED", "true")
    topic = "AI agents and persistent memory"
    assumptions = load_assumptions()
    selected = select_assumptions(topic, "ai", assumptions)
    matches = select_canon_context(
        topic,
        "ai",
        load_canon_files(),
        selected,
    )

    crew, final_task = crew_module.build_research_crew(
        topic,
        "ai",
        7,
        selected,
        matches,
        verbose=False,
    )

    assert len(crew.agents) == 6
    assert len(crew.tasks) == 6
    assert crew.tasks[-2].output_pydantic is crew_module.ImplementationPacket
    assert final_task.output_pydantic is ResearchBrief
    assert all(agent.allow_delegation is False for agent in crew.agents)


def test_github_workflow_runs_daily() -> None:
    workflow = (
        Path(__file__).parents[1] / ".github" / "workflows" / "research-agent.yml"
    ).read_text(encoding="utf-8")
    assert 'cron: "0 16 * * *"' in workflow
    assert "tools.research_crew" in workflow
    assert "requirements-research-crew.txt" in workflow
    assert "OPENAI_API_KEY is not configured" in workflow
