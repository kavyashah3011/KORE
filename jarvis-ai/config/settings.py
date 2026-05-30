"""
Configuration and settings loader.
"""
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
import os


@dataclass
class Settings:
    gemini_api_key: str
    log_file: Path
    data_dir: Path

    @staticmethod
    def load() -> "Settings":
        base = Path(__file__).resolve().parents[1]
        env_path = base / ".env"
        if env_path.exists():
            load_dotenv(env_path)
        gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        data_dir = base / "data"
        log_file = data_dir / "logs" / "jarvis.log"
        return Settings(gemini_api_key=gemini_api_key, log_file=log_file, data_dir=data_dir)
