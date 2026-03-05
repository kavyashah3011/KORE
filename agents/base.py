from __future__ import annotations

"""Shared LLM factory using free Ollama models."""

from langchain_community.llms import Ollama
from config.settings import OLLAMA_MODEL, OLLAMA_BASE_URL


def make_llm(temperature: float = 0.2) -> Ollama:
    """Return a configured Ollama LLM instance (free, runs locally)."""
    return Ollama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=temperature,
        num_predict=4096,  # max output tokens
    )
