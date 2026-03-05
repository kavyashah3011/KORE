from __future__ import annotations

"""Agent specialising in conducting structured web-based research."""
from crewai import Agent
from agents.base import make_llm
from tools.search_tool import web_search_tool


class ResearcherAgent:
    def build(self) -> Agent:
        return Agent(
            role="Research Specialist",
            goal=(
                "Gather comprehensive, accurate, and up-to-date information "
                "on any given topic. Identify key facts, trends, stakeholders, "
                "and potential challenges."
            ),
            backstory=(
                "You are a meticulous research analyst with 15 years of experience "
                "synthesising complex information from diverse sources into structured, "
                "actionable intelligence reports. You leave no stone unturned."
            ),
            llm=make_llm(temperature=0.1),
            tools=[web_search_tool],
            verbose=True,
            allow_delegation=False,
            max_iter=5,
        )
