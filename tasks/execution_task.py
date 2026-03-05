from __future__ import annotations

"""Factory for the execution task used by the Crew pipeline."""

from crewai import Task, Agent
from typing import List


def make_execution_task(agent: Agent, context: List[Task]) -> Task:
    return Task(
        description=(
            "Execute the action plan to accomplish the goal:\n\n"
            "  GOAL: {goal}\n\n"
            "For each phase in the plan:\n"
            "  1. Work through every key action step-by-step\n"
            "  2. Produce the concrete deliverable for that phase\n"
            "     (e.g. draft documents, frameworks, code outlines, templates)\n"
            "  3. Note any blockers, assumptions, or deviations\n\n"
            "Save your execution log to a file named 'kore_execution_log.txt' "
            "using the file write tool.\n\n"
            "Be thorough — this output is what the Reviewer will judge."
        ),
        expected_output=(
            "A detailed execution log documenting: what was done in each phase, "
            "concrete deliverables produced, blockers encountered, and any deviations "
            "from the original plan. Also saved to kore_execution_log.txt."
        ),
        agent=agent,
        context=context,
    )
