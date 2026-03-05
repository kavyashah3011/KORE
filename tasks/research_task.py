from __future__ import annotations

"""Factory for the research task used by the Crew pipeline."""

from crewai import Task, Agent


def make_research_task(agent: Agent) -> Task:
    return Task(
        description=(
            "Conduct thorough research on the following goal:\n\n"
            "  GOAL: {goal}\n\n"
            "Your research must cover:\n"
            "  1. Background and current state of the domain\n"
            "  2. Key players, tools, and frameworks involved\n"
            "  3. Emerging trends and recent developments (2024–2025)\n"
            "  4. Major challenges and risks\n"
            "  5. Opportunities worth pursuing\n\n"
            "Use web search to gather up-to-date, factual information. "
            "Cite sources where possible."
        ),
        expected_output=(
            "A structured research report with sections: "
            "Overview, Key Players & Tools, Trends, Challenges, Opportunities. "
            "Minimum 500 words. Factual and well-organised."
        ),
        agent=agent,
    )
