"""
Prompt templates for Gemini to return structured JSON intent.
"""
from typing import Any


INTENT_PROMPT = (
    "You are an intent parser. Receive a user command and output a JSON object describing the intent. "
    "Only output valid JSON and nothing else. The JSON keys must include 'action' and optionally 'app' or 'query'. "
    "Supported actions: open_app, search, time, date, exit, stop. "
    "Examples:\n1) 'Open Chrome' -> {\"action\": \"open_app\", \"app\": \"chrome\"}\n"
    "2) 'Search artificial intelligence' -> {\"action\": \"search\", \"query\": \"artificial intelligence\"}\n"
)


def build_prompt(command_text: str) -> str:
    """Construct a prompt for the Gemini model.

    Args:
        command_text: Raw user speech converted to text.

    Returns:
        Prompt string.
    """
    return f"{INTENT_PROMPT}\nUser: {command_text}\nJSON:" 
