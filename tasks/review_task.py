from __future__ import annotations

"""Factory for the review task used by the Crew pipeline."""

from crewai import Task, Agent
from typing import List


def make_review_task(agent: Agent, context: List[Task]) -> Task:
    return Task(
        description=(
            "Conduct a full quality review of the entire KORE pipeline output "
            "for the goal:\n\n"
            "  GOAL: {goal}\n\n"
            "Your review must assess:\n"
            "  1. Research quality — accuracy, completeness, source credibility\n"
            "  2. Plan quality — clarity, feasibility, specificity, risk coverage\n"
            "  3. Execution quality — thoroughness, deliverable quality, log clarity\n"
            "  4. Goal alignment — does the final output actually achieve the goal?\n"
            "  5. Overall score — rate each area 1–10 with justification\n\n"
            "Conclude with:\n"
            "  - A final overall score (1–10)\n"
            "  - Top 3 strengths\n"
            "  - Top 3 improvements needed\n"
            "  - Final recommendation: APPROVE / REVISE / REJECT\n\n"
            "Save the review to 'kore_review_report.txt' using the file write tool."
        ),
        expected_output=(
            "A structured quality review report with scored assessments for each area, "
            "an overall score, strengths, improvement recommendations, and a final "
            "APPROVE / REVISE / REJECT decision. Saved to kore_review_report.txt."
        ),
        agent=agent,
        context=context,
    )
