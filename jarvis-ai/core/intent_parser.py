"""
Validate and normalize intent JSON returned by Brain.
"""
from typing import Any, Dict, Optional
from utils.constants import SUPPORTED_ACTIONS
import logging


class IntentParser:
    """Ensure required fields exist and normalize values."""

    def __init__(self, logger: logging.Logger) -> None:
        self.logger = logger

    def parse(self, payload: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Validate payload and return normalized intent or None.

        Args:
            payload: The decoded JSON from the LLM.
        """
        if not payload or not isinstance(payload, dict):
            self.logger.error("Intent payload is invalid: %s", payload)
            return None
        action = payload.get("action")
        if not action or action not in SUPPORTED_ACTIONS:
            self.logger.error("Unsupported or missing action: %s", action)
            return None
        intent = {"action": action}
        # optional fields
        if "app" in payload:
            intent["app"] = payload.get("app")
        if "query" in payload:
            intent["query"] = payload.get("query")
        return intent
