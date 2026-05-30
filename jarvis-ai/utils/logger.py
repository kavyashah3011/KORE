"""
Logger utility to centralize logging configuration.
"""
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def setup_logging(log_file: Optional[Path] = None) -> logging.Logger:
    """Configure a root logger writing to console and a rotating file.

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger("jarvis")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        fh = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=3)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
