from __future__ import annotations

"""Agent that executes the action plan and uses file tools to log results."""
from crewai import Agent
from agents.base import make_llm
from tools.file_tool import file_write_tool, file_read_tool


class ExecutorAgent:
    def build(self) -> Agent:
        return Agent(
            role="Execution Specialist",
            goal=(
                "Execute each phase of the action plan accurately and thoroughly. "
                "Produce concrete deliverables, document every step taken, "
                "and immediately surface any blockers or deviations from the plan."
            ),
            backstory=(
                "You are a highly reliable operations lead with a bias for action. "
                "You turn strategic plans into real outputs — you write, build, document, "
                "and deliver. You always log your work so it can be reviewed and improved."
            ),
            llm=make_llm(temperature=0.1),
            tools=[file_write_tool, file_read_tool],
            verbose=True,
            allow_delegation=False,
            max_iter=6,
        )
