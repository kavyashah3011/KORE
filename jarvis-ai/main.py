"""
Entry point for JARVIS assistant.

Run `python main.py` after installing requirements and adding a .env with GEMINI_API_KEY.
"""
from config.settings import Settings
from core.assistant import Assistant
from utils.logger import setup_logging


def main() -> None:
    """Start the assistant."""
    settings = Settings.load()
    logger = setup_logging(settings.log_file)
    assistant = Assistant(settings=settings, logger=logger)
    assistant.start()


if __name__ == "__main__":
    main()
