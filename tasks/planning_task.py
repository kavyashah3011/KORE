from __future__ import annotations

"""Factory for the planning task used by the Crew pipeline."""

from crewai import Task, Agent
from typing import List


def make_planning_task(agent: Agent, context: List[Task]) -> Task:
    return Task(
        description=(
            "Using the research findings provided, create a detailed action plan "
            "to accomplish this goal:\n\n"
            "  GOAL: {goal}\n\n"
            "Your plan must include:\n"
            "  1. Executive summary (2–3 sentences)\n"
            "  2. Phase breakdown (minimum 3 phases)\n"
            "     — For each phase: name, objective, key actions, owner, timeline, KPIs\n"
            "  3. Resource requirements (people, tools, budget estimate)\n"
            "  4. Risk register (top 3 risks + mitigation)\n"
            "  5. Definition of Done — how we know the goal is achieved\n\n"
            "Be specific and realistic. Base your plan on the research context."
        ),
        expected_output=(
            "A phased action plan document with executive summary, phase breakdown, "
            "resource requirements, risk register, and success criteria. "
            "Structured, specific, and actionable."
        ),
        agent=agent,
        context=context,
    )
