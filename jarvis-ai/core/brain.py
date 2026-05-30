"""
Brain module: talks to Gemini (Google Generative AI) and returns structured intent.
"""
from typing import Any, Dict, Optional
from config.prompts import build_prompt
from config.settings import Settings
from utils.helpers import safe_json_loads
import logging


class Brain:
    """Encapsulates calls to the Gemini API and parsing of responses.

    If an API key is not provided, the Brain will return a helpful error message
    rather than crashing.
    """

    def __init__(self, settings: Settings, logger: logging.Logger) -> None:
        self.settings = settings
        self.logger = logger
        self.client = None
        try:
            import google.generativeai as genai  # type: ignore

            genai.configure(api_key=settings.gemini_api_key)
            self.client = genai
        except Exception as e:
            self.logger.warning("Gemini client not configured: %s", e)

    def parse_intent(self, user_text: str) -> Dict[str, Any]:
        """Send prompt to Gemini and parse returned JSON intent.

        Returns a dict with keys `success` (bool), `intent` (dict|None), and `raw` (str).
        """
        prompt = build_prompt(user_text)
        raw = ""
        if not self.client or not self.settings.gemini_api_key:
            self.logger.warning("No Gemini API key; using local fallback parser.")
            # Very small heuristic fallback
            raw = self._fallback_intent(user_text)
        else:
            try:
                # Using google.generativeai chat API
                resp = self.client.chat.create(model="gemini-lite", input=prompt)
                raw = getattr(resp, "content", None) or str(resp)
            except Exception as e:
                self.logger.exception("Gemini API call failed: %s", e)
                raw = ""

        intent = safe_json_loads(raw)
        if intent is None:
            return {"success": False, "intent": None, "raw": raw}
        return {"success": True, "intent": intent, "raw": raw}

    def _fallback_intent(self, text: str) -> str:
        """Naive local parser that returns a JSON string for simple commands."""
        import json
        t = text.lower().strip()
        if any(w in t for w in ("exit", "quit", "stop jarvis", "stop")):
            return json.dumps({"action": "exit"})
        if "time" in t:
            return json.dumps({"action": "time"})
        if "date" in t or "today" in t:
            return json.dumps({"action": "date"})
        if t.startswith("open "):
            app = t.replace("open ", "").strip()
            return json.dumps({"action": "open_app", "app": app})
        if t.startswith("search ") or t.startswith("google "):
            q = t.replace("search ", "").replace("google ", "").strip()
            return json.dumps({"action": "search", "query": q})
        return json.dumps({"action": "unknown"})
