# FREE LLM OPTIONS FOR KORE - COMPARISON GUIDE

## 🎯 Quick Decision: Which to Use?

| Use Case | Recommendation |
|----------|-----------------|
| **Want completely free, no limits?** | ✅ **Ollama** (runs locally) |
| **Don't want to install software?** | ✅ **Groq** (cloud API) |
| **Have old/weak computer?** | ✅ **Groq** (less RAM needed) |
| **Want to learn AI locally?** | ✅ **Ollama** (education friendly) |
| **Need fastest speed?** | ✅ **Groq** (optimized for speed) |
| **Maximum privacy?** | ✅ **Ollama** (stays on your machine) |

---

## Option 1: OLLAMA (Recommended - Completely Free)

### ✅ Advantages
- **100% free** - No API costs ever, no billing
- **Unlimited requests** - Use as much as you want
- **Works offline** - No internet needed after setup
- **Local privacy** - Data never leaves your computer
- **Open source** - Fully transparent
- **Educational** - Great for learning

### ⚠️ Disadvantages
- Requires installation (5-10 min)
- Uses local RAM (4-16 GB depending on model)
- Slower than cloud APIs (but still reasonable)
- GPU helps but not required

### 📥 Installation (5 minutes)

```bash
# 1. Download & install Ollama from https://ollama.ai

# 2. Download a model (choose ONE based on your RAM):
ollama pull mistral      # 4-8GB (RECOMMENDED - good balance)
# OR
ollama pull llama2       # 8-16GB (more powerful)
# OR
ollama pull orca-mini    # 3-4GB (smaller, less capable)

# 3. Start the Ollama server (keep this running)
ollama serve

# 4. In .env file, set:
OLLAMA_MODEL=mistral
OLLAMA_BASE_URL=http://localhost:11434

# 5. Run KORE
python main.py
```

### 🔧 Configuration (`.env`)

```env
# Model you downloaded
OLLAMA_MODEL=mistral

# Server URL (localhost for your computer)
OLLAMA_BASE_URL=http://localhost:11434

# Temperature (creativity)
OLLAMA_TEMP_LOW=0.1
OLLAMA_TEMP_MED=0.3
```

### 📊 Model Comparison

| Model | Size | Speed | Quality | RAM | Best For |
|-------|------|-------|---------|-----|----------|
| **Mistral** | 7B | Very Fast | Good | 4-8 GB | General tasks (RECOMMENDED) |
| Llama 2 | 7-70B | Medium | Good | 8-16 GB | Complex reasoning |
| Neural Chat | 7B | Very Fast | Basic | 4 GB | Quick tasks |
| Orca Mini | 3B | Lightning | Fair | 3 GB | Very low RAM |
| Zephyr | 7B | Fast | Excellent | 8 GB | High quality output |

---

## Option 2: GROQ (Free Cloud API)

### ✅ Advantages
- **No installation needed** - Works immediately
- **Cloud-based** - Works from any machine
- **Very fast** - Optimized inference
- **Good free tier** - 500+ requests/day
- **Low RAM** - No local resources needed
- **Reliable** - Enterprise infrastructure

### ⚠️ Disadvantages
- Requires API key (sign up ~2 min)
- Has rate limits (500 requests/day free)
- Data sent to cloud (minor privacy concern)
- Limited model selection
- Internet required always

### 📥 Setup (2 minutes)

```bash
# 1. Get FREE API key (no credit card):
#    - Go to https://console.groq.com/keys
#    - Sign up with Google/GitHub
#    - Copy your API key

# 2. Install required package:
pip install langchain-groq

# 3. Create/edit .env file:
GROQ_API_KEY=your-free-api-key-from-groq
GROQ_MODEL=mixtral-8x7b-32768

# 4. Update agents/base.py (code below)

# 5. Run KORE
python main.py
```

### 🔧 Configuration

**`.env` file:**
```env
# Get from https://console.groq.com/keys
GROQ_API_KEY=gsk_...your_key_here...

# Available models:
GROQ_MODEL=mixtral-8x7b-32768    # Balanced
# GROQ_MODEL=llama2-70b-4096     # Powerful
# GROQ_MODEL=gemma-7b-it         # Lightweight
```

**Update `agents/base.py`:**

Replace the entire file with:

```python
from __future__ import annotations

"""Shared LLM factory using free Groq API."""

from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY, GROQ_MODEL

def make_llm(temperature: float = 0.2) -> ChatGroq:
    """Return a configured Groq LLM instance (free API)."""
    return ChatGroq(
        model=GROQ_MODEL,
        api_key=GROQ_API_KEY,
        temperature=temperature,
    )
```

**Update `config/settings.py`:**

Replace these lines:
```python
# OLD (Ollama):
OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral")
OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# NEW (Groq):
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
GROQ_MODEL: str = os.getenv("GROQ_MODEL", "mixtral-8x7b-32768")
```

---

## Option 3: HYBRID (Use Both!)

You can even switch between them:

```bash
# Run with Ollama
OLLAMA_MODEL=mistral python main.py

# Switch to Groq if you hit Ollama issues
GROQ_API_KEY=your-key python main.py
```

---

## Troubleshooting

### Ollama Issues

| Problem | Solution |
|---------|----------|
| `refused to connect` | Make sure Ollama server is running (`ollama serve`) |
| `out of memory` | Use smaller model (`ollama pull orca-mini`) |
| `slow inference` | Add GPU support or use Groq instead |
| `model not found` | Download it first (`ollama pull mistral`) |

### Groq Issues

| Problem | Solution |
|---------|----------|
| `API key invalid` | Get new key from https://console.groq.com/keys |
| `rate limit exceeded` | Free tier has 500 req/day limit, wait for reset |
| `model unavailable` | Check available models at groq.com docs |
| `no internet` | Groq requires internet, use Ollama offline |

---

## Cost Comparison

| Service | Cost | Limit |
|---------|------|-------|
| **Ollama** | $0 | Unlimited |
| **Groq** | $0 | 500 requests/day (free) |
| ~~Claude API~~ | $5-20/month | Varies |
| ~~ChatGPT API~~ | $1-5/month | Pay per use |

---

## Recommendations by Scenario

### Scenario 1: "I'm testing KORE"
→ Use **Groq** (instant setup, no installation)

### Scenario 2: "I run KORE daily"
→ Use **Ollama** (unlimited, no costs)

### Scenario 3: "I want best quality"
→ Use **Ollama with Zephyr model** (excellent output)

### Scenario 4: "I have weak computer"
→ Use **Groq** (cloud-based, minimal local resources)

### Scenario 5: "I want maximum privacy"
→ Use **Ollama** (everything local, no cloud)

### Scenario 6: "I want absolute fastest"
→ Use **Groq** (optimized inference servers)

---

## Model Quality Ranking

From best quality to fastest:

1. **Mistral 8x7B** (Groq) - Best overall
2. **Zephyr 7B** (Ollama) - Excellent local option
3. **Llama 2 70B** (Ollama) - Most powerful
4. **Mixtral 8x7B** (Groq) - Fast & good quality
5. **Neural Chat 7B** (Ollama) - Good balance
6. **Orca Mini 3B** (Ollama) - Fast but basic

---

## Next Steps

1. **Choose your option** (Ollama or Groq)
2. **Follow the setup** in this guide
3. **Update .env file** with your settings
4. **Run `python main.py`** and enjoy! 🎉

---

Questions? Check the main README.md for more details!
