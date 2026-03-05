from __future__ import annotations

"""Agent that reviews the pipeline outputs and produces a scored report."""
from crewai import Agent
from agents.base import make_llm
from tools.file_tool import file_write_tool


class ReviewerAgent:
    def build(self) -> Agent:
        return Agent(
            role="Quality Reviewer",
            goal=(
                "Critically assess the full pipeline output — research, plan, and execution — "
                "for accuracy, completeness, internal consistency, and alignment with the "
                "original goal. Produce a scored review with clear recommendations."
            ),
            backstory=(
                "You are a principal-level quality assurance expert who has reviewed hundreds "
                "of strategic deliverables. You have a sharp eye for gaps, logical inconsistencies, "
                "unsupported claims, and missed opportunities. Your reviews are trusted as the "
                "definitive final word on quality."
            ),
            llm=make_llm(temperature=0.2),
            tools=[file_write_tool],
            verbose=True,
            allow_delegation=False,
            max_iter=4,
        )
