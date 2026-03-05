# KORE — Multi-Agent Collaboration Pipeline

> **An intelligent multi-agent system that researches topics, creates strategic plans, executes tasks, and reviews quality using Claude AI**

**Stack:** Claude (reasoning) · CrewAI (orchestration) · LangChain (tools) · DuckDuckGo (web search)

---

## 📋 Table of Contents

1. [What is KORE?](#what-is-kore)
2. [System Requirements](#system-requirements)
3. [Complete Folder Structure](#complete-folder-structure)
4. [File Descriptions](#file-descriptions)
5. [Installation & Setup](#installation--setup)
6. [Configuration Details](#configuration-details)
7. [How Agents Work](#how-agents-work)
8. [Running KORE](#running-kore)
9. [Understanding Outputs](#understanding-outputs)
10. [Customization Guide](#customization-guide)
11. [Testing](#testing)
12. [Troubleshooting](#troubleshooting)
13. [Command Reference](#command-reference)

---

## What is KORE?

KORE is a **multi-agent AI system** that breaks down complex goals into structured workflows:

1. **🔍 Researcher** - Gathers factual information via web search
2. 📋 **Planner** - Creates phased action plans with KPIs and risks
3. ⚙️ **Executor** - Implements the plan and produces deliverables  
4. ✅ **Reviewer** - Audits quality and scores the entire output

Each agent uses **Claude AI** for reasoning and passes context to the next agent, creating an intelligent pipeline that handles research-to-execution workflows.

---

## System Requirements

- **Python**: 3.10 or higher
- **API**: Anthropic Claude API key (get at https://console.anthropic.com)
- **OS**: Windows, macOS, or Linux
- **Internet**: Required for web search and API calls

---

## Complete Folder Structure

```
KORE-legend/
│
├── 📄 main.py                          ← ENTRY POINT: Run this to start pipeline
├── 📄 crew.py                          ← Orchestrator: wires agents & tasks together
├── 📄 requirements.txt                 ← All Python dependencies
├── 📄 .env.example                     ← Template for environment variables
├── 📄 README.md                        ← This file
│
├── 📁 config/                          ← Configuration module
│   ├── __init__.py
│   └── settings.py                     ← Load env vars, set paths, configure models
│
├── 📁 agents/                          ← Agent definitions
│   ├── __init__.py
│   ├── base.py                         ← Shared LLM factory (Claude config)
│   ├── researcher.py                   ← Research Specialist agent
│   ├── planner.py                      ← Strategic Planner agent
│   ├── executor.py                     ← Execution Specialist agent
│   └── reviewer.py                     ← Quality Reviewer agent
│
├── 📁 tasks/                           ← Task definitions for each agent
│   ├── __init__.py
│   ├── research_task.py                ← Research task prompt & config
│   ├── planning_task.py                ← Planning task prompt & config
│   ├── execution_task.py               ← Execution task prompt & config
│   └── review_task.py                  ← Review task prompt & config
│
├── 📁 tools/                           ← Tools agents can use
│   ├── __init__.py
│   ├── search_tool.py                  ← DuckDuckGo web search wrapper
│   └── file_tool.py                    ← File I/O tools (write/read/scan)
│
├── 📁 tests/                           ← Unit tests
│   ├── test_file_tool.py               ← Tests for file utilities
│
├── 📁 outputs/                         ← Generated outputs (auto-created)
│   ├── kore_execution_log.txt          ← Executor writes step-by-step log
│   └── kore_review_report.txt          ← Reviewer writes final report
│
└── 📁 logs/                            ← Execution logs (auto-created)
    └── kore.log                        ← Full run log with timestamps
```

---

## File Descriptions

### Core Files

| File | Purpose | Key Classes/Functions |
|------|---------|----------------------|
| `main.py` | Entry point that runs the entire pipeline | `main()` |
| `crew.py` | Orchestrates agents into a workflow | `KORECrew` class |
| `requirements.txt` | Python package dependencies | (pip install list) |
| `.env.example` | Template for secrets/config | (copy to `.env`) |

### Config Module (`config/`)

| File | Purpose | Key Config |
|------|---------|-----------|
| `settings.py` | Central config source | `KORE_GOAL`, `CLAUDE_MODEL`, `BASE_DIR`, `LOGS_DIR`, `OUTPUTS_DIR` |

### Agents Module (`agents/`)

| File | Agent Role | Tools | Temperature |
|------|-----------|-------|------------|
| `base.py` | LLM factory | N/A | N/A |
| `researcher.py` | Research Specialist (gathers info) | Web search | 0.1 (conservative) |
| `planner.py` | Strategic Planner (creates action plan) | None | 0.3 (balanced) |
| `executor.py` | Execution Specialist (does the work) | File I/O | 0.1 (conservative) |
| `reviewer.py` | Quality Reviewer (scores output) | File I/O | 0.2 (balanced) |

### Tasks Module (`tasks/`)

| File | Task | Input | Output |
|------|------|-------|--------|
| `research_task.py` | Research the goal | Goal | Research report (500+ words) |
| `planning_task.py` | Create action plan | Research output | Phased plan with KPIs |
| `execution_task.py` | Execute the plan | Plan output | Deliverables + log |
| `review_task.py` | Quality review | All above outputs | Scored report + recommendation |

### Tools Module (`tools/`)

| File | Function | Key Features |
|------|----------|--------------|
| `search_tool.py` | `web_search_tool()` | DuckDuckGo search, error handling |
| `file_tool.py` | `file_write_tool()` / `file_read_tool()` / `find_python_files()` | Safe file I/O, repo scanning |

---

## Installation & Setup

### Step 1: Clone/Download Repository

```bash
# Navigate to project directory
cd KORE-legend
```

### Step 2: Create Python Virtual Environment

```powershell
# Windows PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
# Install all required packages from requirements.txt
pip install -r requirements.txt

# Verify installation (should not error)
pip list | grep crewai
```

**What gets installed:**
- `crewai` - Multi-agent orchestration
- `langchain` - LLM framework
- `langchain-anthropic` - Claude integration
- `langchain-community` - DuckDuckGo search
- `duckduckgo-search` - Web search library
- `anthropic` - Anthropic API client
- `python-dotenv` - Environment variable loading
- `pydantic` - Data validation
- `rich` - Terminal formatting
- `pytest` - Testing framework

### Step 4: Get Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com)
2. Sign in or create account
3. Navigate to **API Keys** section
4. Create new API key and copy it
5. **Never share this key publicly**

### Step 5: Create `.env` File

```bash
# Copy the example file
cp .env.example .env

# Open .env and add your API key:
```

**`.env` file contents:**
```env
# Required: Your Anthropic Claude API key
ANTHROPIC_API_KEY=sk-ant-v5-your-actual-key-here-1234567890abcdef

# Optional: Override the Claude model (defaults to claude-sonnet-4-20250514)
CLAUDE_MODEL=claude-sonnet-4-20250514

# Optional: Set your goal (can also override with env var at runtime)
KORE_GOAL=Research the current state of AI agent frameworks in 2025, create an actionable adoption plan for a mid-sized tech startup, and produce a quality-reviewed final report.

# Optional: Temperature settings (affects randomness of responses)
CLAUDE_TEMP_LOW=0.1
CLAUDE_TEMP_MED=0.3
```

---

## Configuration Details

### What Each Setting Does

**In `config/settings.py`:**

```python
# Goal for the pipeline (what agents will work on)
KORE_GOAL: str = os.getenv("KORE_GOAL", "default goal here")

# Claude model to use (check Anthropic docs for latest)
CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")

# Temperature: Lower = more focused, Higher = more creative
CLAUDE_TEMP_LOW = 0.1      # Research & Execution (factual)
CLAUDE_TEMP_MED = 0.3      # Planning & Review (balanced)

# Directories for outputs and logs (auto-created)
BASE_DIR    = project root
LOGS_DIR    = ./logs/       (execution logs)
OUTPUTS_DIR = ./outputs/    (generated files)
```

### Override Goal at Runtime

**Option 1: Command Line (Windows PowerShell)**
```powershell
$env:KORE_GOAL="Build a data pipeline for real-time analytics"
python main.py
```

**Option 2: Command Line (Linux/macOS)**
```bash
export KORE_GOAL="Build a data pipeline for real-time analytics"
python main.py
```

**Option 3: Edit `.env` file**
```env
KORE_GOAL=Your custom goal here
```

---

## How Agents Work

### Agent Flow Diagram

```
START
  │
  ├─────────────────────────────────────────────┐
  │                                             │
  v                                             │
[1️⃣ RESEARCHER]                                │
  │ Role: Gathers comprehensive factual        │
  │ information via web search                 │
  │ Tools: DuckDuckGo search                   │
  │ Output: Structured research report         │
  │                                             │
  └─────────────────────────────────────────────┘
                    │
                    v
[2️⃣ PLANNER]
  │ Takes: Research findings
  │ Role: Creates detailed action plan
  │ Tools: None (pure reasoning)
  │ Output: Phased plan with KPIs, risks
  │
  └─────────────────────────────────────────────┐
                                                │
                                                v
[3️⃣ EXECUTOR]
  │ Takes: Action plan
  │ Role: Implements plan & produces results
  │ Tools: File I/O (write/read)
  │ Output: Deliverables + execution log
  │
  └─────────────────────────────────────────────┐
                                                │
                                                v
[4️⃣ REVIEWER]
  │ Takes: All previous outputs
  │ Role: Audits quality & scores everything
  │ Tools: File I/O (write/read)
  │ Output: Scored review report + APPROVE/REVISE/REJECT
  │
  └─────────────────────────────────────────────┐
                                                │
                                                v
                                              END
```

### Each Agent Explained

#### 1️⃣ **Researcher Agent**
- **Job**: Find accurate, current information on the goal topic
- **How**: Uses DuckDuckGo to search the web
- **Temperature**: 0.1 (very focused, factual)
- **Max iterations**: 5 search cycles
- **Output**: Research report with multiple sections

**Generates report covering:**
- Overview of the domain
- Key players & tools
- Emerging trends
- Major challenges
- Opportunities

#### 2️⃣ **Planner Agent**
- **Job**: Transform research into a structured plan
- **How**: Pure reasoning (no tools needed)
- **Temperature**: 0.3 (balanced reasoning)
- **Max iterations**: 4 planning cycles
- **Output**: Executive summary + phased action plan

**Creates plan with:**
- Executive summary (2-3 sentences)
- 3+ phases with: objective, actions, owner, timeline, KPIs
- Resource requirements
- Risk register with mitigations
- Definition of Done metrics

#### 3️⃣ **Executor Agent**
- **Job**: Carry out the plan and produce deliverables
- **How**: Uses file tools to write results
- **Temperature**: 0.1 (precise execution)
- **Max iterations**: 6 execution cycles
- **Output**: Execution log + all deliverables

**Produces:**
- Phase-by-phase execution details
- Concrete deliverables (documents, plans, templates)
- Blockers and deviations noted
- Full execution log saved to file

#### 4️⃣ **Reviewer Agent**
- **Job**: Quality assurance for entire pipeline
- **How**: Uses file tools to write review
- **Temperature**: 0.2 (careful scoring)
- **Max iterations**: 4 review cycles
- **Output**: Scored quality report

**Reviews each area (1-10 scores):**
- Research quality: accuracy, completeness, credibility
- Plan quality: clarity, feasibility, specificity
- Execution quality: thoroughness, deliverables, log clarity
- Goal alignment: does output actually achieve the goal?

**Final recommendation:** `APPROVE` / `REVISE` / `REJECT`

---

## Running KORE

### Basic Run (Default Goal)

```powershell
# Activate environment
.\venv\Scripts\Activate.ps1

# Run pipeline
python main.py
```

**Expected output:**
```
[KORE banner displays]
🎯 Goal: Research the current state of AI agent frameworks...
[Agents run in sequence, each logging progress]
[Files written to outputs/ and logs/]
```

### Run with Custom Goal

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
$env:KORE_GOAL="Design a mobile app for remote team management"
python main.py
```

**Linux/macOS:**
```bash
source venv/bin/activate
export KORE_GOAL="Design a mobile app for remote team management"
python main.py
```

### Run with Longer Timeout (API slowness)

```powershell
# Some goals take 15+ minutes
$env:KORE_GOAL="Write a comprehensive guide to machine learning"
python main.py
```

### View Logs in Real-Time

**While running in another terminal:**
```powershell
# Follow logs as they're written
Get-Content logs\kore.log -Wait
```

---

## Understanding Outputs

### Output Files Location

All outputs saved to `outputs/` directory:

```
outputs/
├── kore_execution_log.txt      ← What executor did (save by executor)
└── kore_review_report.txt      ← Final verdict (saved by reviewer)
```

### Execution Log Example

**File: `outputs/kore_execution_log.txt`**

```
PHASE 1: Research & Discovery
────────────────────────────
Objective: Identify current state of AI agents

Actions Taken:
1. Searched for "AI agent frameworks 2024"
2. Analyzed CrewAI, AutoGen, LangChain
3. Identified 15+ key players
4. Documented emerging trends

Deliverable: research_summary.md
Status: ✓ Complete

...more phases...
```

### Review Report Example

**File: `outputs/kore_review_report.txt`**

```
KORE QUALITY REVIEW REPORT
═════════════════════════════

RESEARCH QUALITY:        8/10
├─ Accuracy: Good, sources verified
├─ Completeness: Covered 90% of domain
└─ Credibility: High (academic + industry sources)

PLAN QUALITY:            7/10
├─ Clarity: Well-structured phases
├─ Feasibility: Realistic timeline (6 months)
└─ Risk Coverage: Top 5 risks identified

EXECUTION QUALITY:       8/10
├─ Thoroughness: All phases delivered
├─ Deliverables: High quality documents
└─ Log Clarity: Detailed step-by-step

GOAL ALIGNMENT:          8/10
└─ Final output aligns 90% with original goal

═════════════════════════════
OVERALL SCORE: 8/10 ⭐⭐⭐⭐

TOP 3 STRENGTHS:
1. Research depth and credibility
2. Clear, actionable plan phases
3. Thorough execution documentation

TOP 3 IMPROVEMENTS:
1. Add competitive analysis to research
2. Include cost-benefit analysis in planning
3. Add success metrics tracking to execution

═════════════════════════════
FINAL RECOMMENDATION: ✅ APPROVE

This output is high quality and ready for
stakeholder presentation with minor additions.
```

### Execution Log in `logs/kore.log`

**File: `logs/kore.log`** (Full detailed log)

```
2024-03-05 14:23:45 INFO Researcher Agent Starting...
2024-03-05 14:23:47 INFO Web search query: "AI agent frameworks 2024"
2024-03-05 14:24:12 INFO Found 47 relevant results
2024-03-05 14:24:15 INFO Planner Agent Starting...
2024-03-05 14:24:52 INFO Plan generated: 5 phases over 6 months
2024-03-05 14:25:00 INFO Executor Agent Starting...
2024-03-05 14:26:30 INFO Written: kore_execution_log.txt
2024-03-05 14:26:35 INFO Reviewer Agent Starting...
2024-03-05 14:27:15 INFO Scores calculated
2024-03-05 14:27:20 INFO Written: kore_review_report.txt
2024-03-05 14:27:21 INFO KORE pipeline complete
```

---

## Customization Guide

### Change the Claude Model

**In `config/settings.py`:**

```python
# Before:
CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")

# After (use Opus for more reasoning):
CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-opus-4-1-20250805")
```

**Or in `.env`:**
```env
CLAUDE_MODEL=claude-opus-4-1-20250805
```

Valid models: `claude-opus`, `claude-sonnet`, `claude-haiku`

### Change Temperature (Creativity) Settings

**In `config/settings.py`:**

```python
# Current (conservative):
CLAUDE_TEMP_LOW = 0.1   # Research & Execution
CLAUDE_TEMP_MED = 0.3   # Planning & Review

# More creative:
CLAUDE_TEMP_LOW = 0.3
CLAUDE_TEMP_MED = 0.5

# Very creative:
CLAUDE_TEMP_LOW = 0.7
CLAUDE_TEMP_MED = 0.9
```

### Add a Custom Agent

**Step 1: Create `agents/analyzer.py`**

```python
from __future__ import annotations

"""Custom analyzer agent for domain analysis."""

from crewai import Agent
from agents.base import make_llm

class AnalyzerAgent:
    def build(self) -> Agent:
        return Agent(
            role="Domain Analyzer",
            goal="Perform deep analysis of specific domain insights",
            backstory="You are expert analyst with 20 years of domain expertise",
            llm=make_llm(temperature=0.2),
            tools=[],  # Add tools here if needed
            verbose=True,
            allow_delegation=False,
            max_iter=4,
        )
```

**Step 2: Create `tasks/analysis_task.py`**

```python
from __future__ import annotations

"""Task for domain analysis."""

from crewai import Task, Agent
from typing import List

def make_analysis_task(agent: Agent, context: List[Task]) -> Task:
    return Task(
        description="Analyze the {goal} from a domain perspective",
        expected_output="In-depth domain analysis report",
        agent=agent,
        context=context,
    )
```

**Step 3: Wire into `crew.py`**

```python
from agents.analyzer import AnalyzerAgent
from tasks.analysis_task import make_analysis_task

class KORECrew:
    def __init__(self):
        # ... existing agents ...
        self.analyzer = AnalyzerAgent().build()
    
    def run(self, goal: str) -> str:
        # ... existing tasks ...
        t_analysis = make_analysis_task(
            self.analyzer,
            context=[t_planning]
        )
        
        crew = Crew(
            agents=[..., self.analyzer],
            tasks=[..., t_analysis],
            process=Process.sequential,
        )
        # ...
```

### Enable Parallel Execution (Hierarchical)

**In `crew.py`:**

```python
# Change from:
process=Process.sequential,

# To:
process=Process.hierarchical,
```

This allows agents to work in parallel with a manager agent coordinating.

### Add Memory Between Runs (Persistence)

**In `crew.py`:**

```python
crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,          # ← Add this
    cache=True,           # ← Add this
)
```

### Enable Human-in-the-Loop Approval

**In any task file (e.g., `tasks/review_task.py`):**

```python
def make_review_task(agent: Agent, context: List[Task]) -> Task:
    return Task(
        description="Review the entire output",
        expected_output="Scored review report",
        agent=agent,
        context=context,
        human_input=True,  # ← Add this to require approval
    )
```

### Adjust Agent Behavior

**In `agents/researcher.py`:**

```python
class ResearcherAgent:
    def build(self) -> Agent:
        return Agent(
            role="Research Specialist",
            goal="...",
            backstory="You are...",
            llm=make_llm(temperature=0.1),
            tools=[web_search_tool],
            verbose=True,
            allow_delegation=False,
            max_iter=5,    # ← Change max iterations
        )
```

---

## Testing

### Run All Tests

```bash
# Activate environment first
.\venv\Scripts\Activate.ps1

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_file_tool.py -v
```

### Test Output

```
tests/test_file_tool.py::test_find_single_file PASSED        [ 25%]
tests/test_file_tool.py::test_find_in_directory PASSED       [ 50%]
tests/test_file_tool.py::test_extensions_filter PASSED       [ 75%]
tests/test_file_tool.py::test_sorting PASSED                 [100%]

======================== 4 passed in 5.05s ========================
```

### Example: Write Your Own Test

**Create `tests/test_crew.py`:**

```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from crew import KORECrew

def test_crew_builds():
    """Test that KORECrew initializes without errors"""
    crew = KORECrew()
    assert crew.researcher is not None
    assert crew.planner is not None
    assert crew.executor is not None
    assert crew.reviewer is not None
```

Run it:
```bash
pytest tests/test_crew.py -v
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'anthropic'`

**Solution:**
```bash
# Activate venv and install
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Issue: `ANTHROPIC_API_KEY not set`

**Solution:**
```bash
# Check .env file exists and has key
type .env

# Or set at runtime
$env:ANTHROPIC_API_KEY="sk-ant-v5-..."
python main.py
```

### Issue: `No internet connection / Search failed`

**Solution:**
- Check your internet connection
- DuckDuckGo was blocked, edit `tools/search_tool.py` to use alternative search
- Or use a VPN

### Issue: `Crew stopped unexpectedly`

**Solution:**
- Check `logs/kore.log` for error details
- Increase timeout (tasks take 10-30 mins)
- Try with smaller goal scope first
- Check API key is valid

### Issue: `What went wrong with my goal?`

**Solution:**
1. Check output files exist:
   ```bash
   dir outputs/
   # Should show: kore_execution_log.txt, kore_review_report.txt
   ```

2. Read the review report:
   ```bash
   type outputs/kore_review_report.txt
   ```

3. Check full log:
   ```bash
   type logs/kore.log
   ```

---

## Command Reference

### Python/Environment Commands

| Command | Purpose |
|---------|---------|
| `python -m venv venv` | Create virtual environment |
| `.\venv\Scripts\Activate.ps1` | Activate venv (Windows) |
| `source venv/bin/activate` | Activate venv (Linux/macOS) |
| `pip install -r requirements.txt` | Install dependencies |
| `pip list` | List installed packages |
| `pip install --upgrade pip` | Update pip |

### Running KORE

| Command | Purpose |
|---------|---------|
| `python main.py` | Run with default goal |
| `$env:KORE_GOAL="..."; python main.py` | Run with custom goal |
| `python -m compileall .` | Check syntax of all files |
| `python -c "from crew import KORECrew; print('OK')"` | Test imports |

### Testing Commands

| Command | Purpose |
|---------|---------|
| `pytest` | Run all tests |
| `pytest -v` | Run with verbose output |
| `pytest tests/test_file_tool.py` | Run specific test file |
| `pytest -k "test_find"` | Run tests matching pattern |
| `pytest --tb=short` | Short traceback on failures |

### File Operations

| Command | Purpose |
|---------|---------|
| `dir outputs/` | List output files |
| `type outputs/kore_review_report.txt` | View review report |
| `type logs/kore.log` | View execution log |
| `del outputs/*` | Clear old outputs |
| `del logs/*` | Clear old logs |

---

## Common Workflows

### Workflow 1: Run Once, Review Results

```powershell
# 1. Activate and set goal
.\venv\Scripts\Activate.ps1
$env:KORE_GOAL="Write a 5-year business strategy for a fintech startup"

# 2. Run
python main.py

# 3. Wait 20-30 minutes...

# 4. Review results
type outputs/kore_review_report.txt

# 5. If good, copy somewhere safe
cp outputs/kore_review_report.txt "C:\Backups\report_$(Get-Date -f 'yyyy-MM-dd').txt"
```

### Workflow 2: Iterate & Improve

```powershell
# 1. Run with goal v1
$env:KORE_GOAL="Create a marketing plan for B2B SaaS"
python main.py

# 2. Review output
type outputs/kore_review_report.txt

# 3. Refine goal based on suggestions
$env:KORE_GOAL="Create a marketing plan for B2B SaaS including: competitive analysis, pricing strategy, go-to-market timeline"
python main.py

# 4. Compare reviews from both runs
```

### Workflow 3: Extract & Process Results

```powershell
# 1. Run
python main.py

# 2. Extract key data programmatically
python -c @"
with open('outputs/kore_execution_log.txt') as f:
    content = f.read()
    print('Key metrics found:', content.count('KPI'))
"@

# 3. Feed into downstream system
# (e.g., save to database, send email alert, etc.)
```

---

## Next Steps

1. **Try the default goal first** to ensure everything works
2. **Define your custom goal** and run the pipeline
3. **Review the outputs** in `outputs/` directory
4. **Customize agents/tasks** based on your needs
5. **Add tests** for any custom logic you write
6. **Deploy** or integrate into your workflow

---

## Support & Resources

- **CrewAI Docs**: https://docs.crewai.com
- **LangChain Docs**: https://python.langchain.com
- **Anthropic Claude API**: https://console.anthropic.com
- **DuckDuckGo Search**: https://duckduckgo.com

---

**Happy researching!** 🚀
```
