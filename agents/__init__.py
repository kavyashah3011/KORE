"""Top-level package for KORE agents.

Each submodule exposes a builder class that returns a configured ``Agent``
from the ``crewai`` library.

The package also exports ``__all__`` for convenience imports.
"""

__all__ = [
    "ResearcherAgent",
    "PlannerAgent",
    "ExecutorAgent",
    "ReviewerAgent",
]