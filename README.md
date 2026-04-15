━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  PIPELINE INTELLIGENCE AGENT
  Live HubSpot deal data → prioritized pipeline report with clear
  action paths.
  by Hans Stewart · hansstewart.dev

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Architecture    →   hansstewart.github.io/ai-architecture
  Portfolio       →   hansstewart.dev
  GitHub          →   github.com/HansStewart/pipeline-intelligence-agent

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
WHAT IT DOES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  A sales-operations intelligence system that connects to HubSpot,
  pulls the live state of all active deals, normalizes the data, and
  uses GPT-4o to produce an actionable pipeline intelligence report —
  automatically, on demand.

  The agent calculates pipeline health, flags stale and overdue deals,
  generates weighted forecast logic, and produces a prioritized list
  of next actions for near-term execution. The output is machine-usable
  JSON designed to feed dashboards, decision flows, and executive reviews
  without a manual analyst in the loop.

  Primary value: automates a senior sales-ops style pipeline analysis in
  real time. Use cases: pipeline reviews, executive reporting, and team
  prioritization.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BACKEND WORKFLOW — 4 STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Step 01 — HubSpot connection
    Authenticates against HubSpot CRM v3 APIs.
    Pulls active deals, stages, dates, values, and core pipeline metadata.
    Collects the working dataset required for sales analysis.
    → Input: Live CRM deal data

  Step 02 — Normalization layer
    Standardizes stage values, dates, and probability context.
    Highlights stale, overdue, and low-momentum opportunities.
    Builds structured inputs for forecasting and prioritization.
    → Intermediate: Clean pipeline dataset

  Step 03 — Intelligence generation
    Uses GPT-4o to calculate pipeline health and identify risk patterns.
    Generates weighted forecast logic and high-priority deal focus.
    Produces recommended next actions for near-term execution.
    → Processing: Health scoring + prioritization

  Step 04 — Report delivery
    Packages forecast, risk flags, and priorities into structured output.
    Returns a machine-usable JSON response for BI and dashboard use.
    Supports real-time pipeline review without manual analyst work.
    → Output: Pipeline intelligence report


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REPORT CONTAINS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Pipeline health score       Overall state of the active deal set
  Risk flags                  Stale, overdue, and low-momentum deals
  Forecast                    Weighted revenue projection by stage
  Priority action list        Ranked next-best actions for near-term
                              execution
  Decision support            Clear flags for risk and forecast strength


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TECH STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Language        Python 3.11
  Framework       Flask
  Server          Gunicorn
  AI Model        OpenAI GPT-4o
  CRM             HubSpot CRM v3 API
  Deployment      Google Cloud Run — us-east1


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
LOCAL DEVELOPMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  git clone https://github.com/HansStewart/pipeline-intelligence-agent.git
  cd pipeline-intelligence-agent
  pip install -r requirements.txt
  cp .env.example .env
  → Add OPENAI_API_KEY and HUBSPOT_API_KEY to .env
  python main.py
  → Open http://localhost:8080


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENVIRONMENT VARIABLES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  OPENAI_API_KEY       required    Intelligence generation and scoring
  HUBSPOT_API_KEY      required    CRM v3 API read access

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Hans Stewart · Marketing Automation Engineer · hansstewart.dev
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━