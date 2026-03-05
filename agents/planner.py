from __future__ import annotations

"""Agent responsible for turning research findings into an executable plan."""
from crewai import Agent
from agents.base import make_llm


class PlannerAgent:
    def build(self) -> Agent:
        return Agent(
            role="Strategic Planner",
            goal=(
                "Transform research findings into a clear, phased action plan "
                "with measurable milestones, resource requirements, risk assessments, "
                "and success criteria for each phase."
            ),
            backstory=(
                "You are a senior strategic consultant who has led complex transformation "
                "programmes at Fortune 500 companies. You excel at breaking down ambitious "
                "goals into precise, executable roadmaps with clear ownership and KPIs."
            ),
            llm=make_llm(temperature=0.3),
            tools=[],
            verbose=True,
            allow_delegation=False,
            max_iter=4,
        )
