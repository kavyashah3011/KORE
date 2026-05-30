# JARVIS — Phase 1 Desktop AI Voice Assistant

JARVIS is a modular Python desktop assistant (Phase 1 MVP) that listens to voice commands,
parses intent using a generative model (Gemini), executes system actions, and replies with
text-to-speech.

## Repository Layout

- `main.py` — Application entrypoint.
- `config/` — Settings and prompts.
- `core/` — Listener, Speaker, Brain (LLM), Intent Parser, Assistant orchestrator.
- `actions/` — Action implementations and router (`open_app`, `search`, `time`, `date`).
- `utils/` — Logger, helpers, constants.
- `data/` — `logs/` and `memory/` (persistence folders).
- `assets/` — placeholders for sounds/icons.
- `tests/` — unit tests.

## Prerequisites

- Python 3.12+
- Microphone access on your machine
- Internet connection for Gemini API calls (optional — fallback parser exists)

## Installation

1. Create a virtual environment (recommended):

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Windows cmd
.\.venv\Scripts\activate.bat
```

2. Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Configure environment variables:

```bash
copy .env.example .env
# Edit .env and set GEMINI_API_KEY=your_key_here
notepad .env
```

If you do not have a Gemini API key, JARVIS will fall back to a simple local intent parser (limited commands).

## Running JARVIS

From the `jarvis-ai/` folder run:

```bash
# Windows PowerShell / cmd
python main.py
```

On startup JARVIS will speak a short greeting and then listen for commands. Example voice commands:

- "Open Chrome"
- "Open Notepad"
- "Open Calculator"
- "Search artificial intelligence"
- "What is the time?"
- "What is today's date?"
- "Exit" / "Stop Jarvis"

## How it works (high level)

1. `core/listener.py` captures microphone audio and uses the `SpeechRecognition` package.
2. `core/brain.py` constructs a prompt via `config/prompts.py` and calls the Gemini API.
3. The assistant expects strict JSON from Gemini; `utils/helpers.py` contains robust JSON parsing fallbacks.
4. `core/intent_parser.py` validates the intent and `actions/action_router.py` dispatches it.
5. `core/speaker.py` uses `pyttsx3` to speak responses.

## Logs

Application logs are written to `data/logs/jarvis.log` (rotating file handler). Ensure the `data/logs/` folder exists (it is created automatically when first run).

## Troubleshooting

- Microphone not found: Ensure your OS has a default microphone and that apps have permission to use it.
- `pyaudio` install issues: On Windows, install prebuilt wheels if pip compilation fails (search for `PyAudio wheels`).
- Gemini API errors: Confirm `GEMINI_API_KEY` in `.env` and network connectivity.
- Applications don't open: Edit `actions/app_actions.py` to provide full executable paths for your system.

## Testing

Run unit tests with:

```bash
python -m unittest discover -v
```

## Development notes & future roadmap

- Add a wake-word detector (local VAD and keyword spotting).
- Integrate Whisper or higher-quality ASR (optional) for offline or higher accuracy.
- Add a GUI (Tkinter prototype) showing status, last command, and response.
- Add a persistent memory store and conversation context.
- Harden intent validation and sandbox potentially dangerous actions.

## Security & Safety

Be cautious granting JARVIS permission to execute system-level commands. The current Phase 1 implementation supports a small fixed action set; do not add arbitrary shell execution without strict validation and user consent.

## Files to review

- `jarvis-ai/main.py` — startup orchestration
- `jarvis-ai/core/brain.py` — LLM integration
- `jarvis-ai/actions/app_actions.py` — application launch mapping

----

If you want, I can now:
- run the unit tests here
- adapt `actions/app_actions.py` with your specific app paths
- add a minimal Tkinter UI prototype

