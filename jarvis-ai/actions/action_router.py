"""
Central action router to dispatch intents to action modules.
"""
from typing import Dict
import logging
from actions import app_actions, web_actions, system_actions


class ActionRouter:
    """Route normalized intents to the proper action and return a response string."""

    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger

    def route(self, intent: Dict[str, str]) -> str:
        action = intent.get("action")
        if action == "open_app":
            app = intent.get("app")
            ok, msg = app_actions.open_app(app or "")
            return msg
        if action == "search":
            query = intent.get("query")
            ok, msg = web_actions.search_google(query or "")
            return msg
        if action == "time":
            ok, msg = system_actions.get_time()
            return msg
        if action == "date":
            ok, msg = system_actions.get_date()
            return msg
        return "I did not understand the requested action."
