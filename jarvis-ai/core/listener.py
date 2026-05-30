"""
Microphone listener using SpeechRecognition.
"""
from typing import Optional
import speech_recognition as sr


class Listener:
    """Listen to microphone and convert speech to text.

    Responsibilities:
    - Capture audio from default microphone
    - Convert to text using recognizer
    - Return text or None on failure
    """

    def __init__(self, logger) -> None:
        self.recognizer = sr.Recognizer()
        self.logger = logger

    def listen(self, timeout: Optional[float] = None, phrase_time_limit: Optional[float] = 8) -> Optional[str]:
        """Listen and return recognized text or None.

        Args:
            timeout: maximum seconds to wait for phrase start.
            phrase_time_limit: maximum seconds for phrase.
        """
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            text = self.recognizer.recognize_google(audio)
            self.logger.info("Heard: %s", text)
            return text
        except sr.WaitTimeoutError:
            self.logger.warning("Listening timed out waiting for phrase start.")
            return None
        except sr.UnknownValueError:
            self.logger.warning("Could not understand audio.")
            return None
        except sr.RequestError as e:
            self.logger.error("Speech recognition request failed: %s", e)
            return None
        except Exception as e:
            self.logger.exception("Unexpected microphone error: %s", e)
            return None
