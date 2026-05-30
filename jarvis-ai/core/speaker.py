"""
Text-to-speech speaker using pyttsx3.
"""
from typing import Optional
import pyttsx3


class Speaker:
    """Responsible for speaking text responses.

    Uses pyttsx3 for offline TTS.
    """

    def __init__(self, logger) -> None:
        self.engine = pyttsx3.init()
        self.logger = logger

    def speak(self, text: str, block: bool = False) -> None:
        """Speak the provided text.

        Args:
            text: The text to speak.
            block: Whether to block until finished.
        """
        try:
            self.logger.info("Speaking: %s", text)
            self.engine.say(text)
            if block:
                self.engine.runAndWait()
            else:
                # run in non-blocking mode
                self.engine.iterate()
        except Exception as e:
            self.logger.exception("TTS failure: %s", e)
