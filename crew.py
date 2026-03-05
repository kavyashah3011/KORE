"""KORE Crew orchestrator.

Wires agents and tasks into a CrewAI sequential pipeline.  Use
``Process.hierarchical`` instead of ``Process.sequential`` for
concurrent, manager-led execution.
"""

from __future__ import annotations

import logging

from crewai import Crew, Process

from agents.researcher import ResearcherAgent
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.reviewer import ReviewerAgent

from tasks.research_task import make_research_task
from tasks.planning_task import make_planning_task
from tasks.execution_task import make_execution_task
from tasks.review_task import make_review_task


class KORECrew:

    def __init__(self):

        self.researcher = ResearcherAgent().build()
        self.planner = PlannerAgent().build()
        self.executor = ExecutorAgent().build()
        self.reviewer = ReviewerAgent().build()

    def run(self, goal: str) -> str:

        logging.info("Building research task")
        t_research = make_research_task(self.researcher)

        logging.info("Building planning task")
        t_planning = make_planning_task(
            self.planner,
            context=[t_research],
        )

        logging.info("Building execution task")
        t_execution = make_execution_task(
            self.executor,
            context=[t_planning],
        )

        logging.info("Building review task")
        t_review = make_review_task(
            self.reviewer,
            context=[t_research, t_planning, t_execution],
        )

        crew = Crew(
            agents=[
                self.researcher,
                self.planner,
                self.executor,
                self.reviewer
            ],

            tasks=[
                t_research,
                t_planning,
                t_execution,
                t_review
            ],

            process=Process.sequential,
            verbose=True,

            memory=True,
            cache=True
        )

        logging.info("Kickoff crew pipeline")
        result = crew.kickoff(inputs={"goal": goal})

        return str(result)