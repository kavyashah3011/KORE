"""
Common helper utilities.
"""
from typing import Any, Optional, Dict
import json
import logging


def safe_json_loads(text: str) -> Optional[Dict[str, Any]]:
    """Attempt to parse JSON from model output robustly.

    Tries multiple fallbacks to be tolerant of common model formatting issues.
    """
    if not text:
        return None
    try:
        return json.loads(text)
    except Exception:
        pass
    # Try to find first JSON substring
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(text[start:end+1])
        except Exception:
            pass
    # Try replacing single quotes
    try:
        cleaned = text.replace("'", '"')
        return json.loads(cleaned)
    except Exception:
        logging.getLogger("jarvis").exception("Failed to parse JSON from model output:")
        return None
