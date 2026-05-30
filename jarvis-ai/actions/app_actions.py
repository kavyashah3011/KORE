"""
Application actions: open common desktop applications.
"""
from typing import Tuple
import subprocess
import shutil
import os
import logging


def open_app(app_name: str, logger: logging.Logger) -> Tuple[bool, str]:
    """Attempt to open a known application by name.

    Returns (success, message)
    """
    app = app_name.lower().strip()
    # common Windows executables
    mapping = {
        "chrome": ["chrome.exe", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"],
        "notepad": ["notepad.exe"],
        "calculator": ["calc.exe", "Calculator.exe"],
        "paint": ["mspaint.exe", "paint.exe"],
    }
    candidates = mapping.get(app, [app_name])
    for candidate in candidates:
        # try full path first
        try:
            if os.path.exists(candidate):
                subprocess.Popen([candidate])
                return True, f"Opened {app_name}."
            path = shutil.which(candidate)
            if path:
                subprocess.Popen([path])
                return True, f"Opened {app_name}."
        except Exception as e:
            logger.exception("Failed to launch %s: %s", candidate, e)
    return False, f"Could not open {app_name}. Make sure it is installed."
