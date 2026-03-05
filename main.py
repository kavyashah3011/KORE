"""KORE — Multi-Agent Collaboration Pipeline
==========================================

Stack : Claude (reasoning) · CrewAI (orchestration) · LangChain (tools)
Flow  : Researcher → Planner → Executor → Reviewer

Usage:
    python main.py
    KORE_GOAL="your goal here" python main.py
"""

from __future__ import annotations

from dotenv import load_dotenv
load_dotenv()

import logging
import os

from crew import KORECrew
from config.settings import KORE_GOAL, BANNER, LOGS_DIR


def main() -> None:
    # configure logging
    os.makedirs(LOGS_DIR, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.FileHandler(os.path.join(LOGS_DIR, "kore.log")),
            logging.StreamHandler(),
        ],
    )

    logging.info(BANNER.replace("\n", " "))
    logging.info(f"🎯  Goal: {KORE_GOAL}")

    crew = KORECrew()
    result = crew.run(goal=KORE_GOAL)

    logging.info("KORE pipeline complete")
    print("\n" + "═" * 64)
    print(result)
    print("═" * 64 + "\n")


if __name__ == "__main__":
    main()
