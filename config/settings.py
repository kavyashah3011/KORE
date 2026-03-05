"""KORE Configuration
==================

All tuneable settings live here.  Override values via environment
variables or a `.env` file.

Using free Ollama models instead of Claude API for zero cost.
"""

from __future__ import annotations

import os
import textwrap

# ── LLM Model (Using Free Ollama) ────────────────────────────────────────────
# Ollama runs locally on your computer - completely FREE!
# Download models at: https://ollama.ai/library
# Popular models: mistral, llama2, neural-chat, orca-mini
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral")
OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# ── Goal ──────────────────────────────────────────────────────────────────────
KORE_GOAL: str = os.getenv(
    "KORE_GOAL",
    "Research the current state of AI agent frameworks in 2025, "
    "create an actionable adoption plan for a mid-sized tech startup, "
    "and produce a quality-reviewed final report.",
)

# ── Temperature Settings ──────────────────────────────────────────────────────
# Lower = more focused, Higher = more creative
OLLAMA_TEMP_LOW = float(os.getenv("OLLAMA_TEMP_LOW", "0.1"))   # Research & Execution
OLLAMA_TEMP_MED = float(os.getenv("OLLAMA_TEMP_MED", "0.3"))   # Planning & Review

# ── Paths ─────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(OUTPUTS_DIR, exist_ok=True)

# ── Banner ────────────────────────────────────────────────────────────────────
BANNER = textwrap.dedent("""
    ██╗  ██╗ ██████╗ ██████╗ ███████╗
    ██║ ██╔╝██╔═══██╗██╔══██╗██╔════╝
    █████╔╝ ██║   ██║██████╔╝█████╗
    ██╔═██╗ ██║   ██║██╔══██╗██╔══╝
    ██║  ██╗╚██████╔╝██║  ██║███████╗
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
    Multi-Agent Collaboration Pipeline (FREE with Ollama)
""")
