"""
Assistant orchestrator: ties listener, brain, parser, action router, and speaker.
"""
from typing import Optional
import logging
from config.settings import Settings
from core.listener import Listener
from core.speaker import Speaker
from core.brain import Brain
from core.intent_parser import IntentParser
from actions.action_router import ActionRouter
import time


class Assistant:
    """High level assistant coordinating components."""

    def __init__(self, settings: Settings, logger: logging.Logger) -> None:
        self.settings = settings
        self.logger = logger
        self.listener = Listener(logger=logger)
        self.speaker = Speaker(logger=logger)
        self.brain = Brain(settings=settings, logger=logger)
        self.parser = IntentParser(logger=logger)
        self.router = ActionRouter(logger=logger)
        self.running = True

    def start(self) -> None:
        """Start the listening loop for the assistant."""
        try:
            self.speaker.speak("J A R V I S online. How can I help?")
        except Exception:
            pass

        while self.running:
            try:
                self.logger.info("Awaiting command...")
                text = self.listener.listen()
                if not text:
                    time.sleep(0.2)
                    continue
                self.logger.info("Command received: %s", text)
                result = self.brain.parse_intent(text)
                if not result.get("success"):
                    self.speaker.speak("Sorry, I couldn't understand that.")
                    continue
                raw_intent = result.get("intent")
                intent = self.parser.parse(raw_intent)
                if not intent:
                    self.speaker.speak("I couldn't interpret the intent.")
                    continue
                # Handle exit locally
                if intent.get("action") == "exit":
                    self.speaker.speak("Goodbye.")
                    self.running = False
                    break

                response_text = self.router.route(intent)
                # Speak and print
                print("JARVIS:", response_text)
                self.speaker.speak(response_text)
            except KeyboardInterrupt:
                self.logger.info("Interrupted by user. Exiting.")
                self.running = False
            except Exception as e:
                self.logger.exception("Assistant loop error: %s", e)
                self.speaker.speak("An error occurred processing your request.")
