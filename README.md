# Pipeline Intelligence Agent

> A sales-operations intelligence system that pulls live HubSpot deal data, analyzes it, and returns a prioritized pipeline report with clear action paths.

**by Hans Stewart &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**

[Architecture](https://hansstewart.github.io/ai-architecture) &nbsp;·&nbsp; [Portfolio](https://hansstewart.dev) &nbsp;·&nbsp; [GitHub](https://github.com/HansStewart/pipeline-intelligence-agent)

---

## What It Does

Connects to HubSpot, pulls the live state of all active deals, normalizes the data, and uses GPT-4o to produce an actionable pipeline intelligence report — automatically, on demand.

The agent calculates pipeline health, flags stale and overdue deals, generates weighted forecast logic, and produces a prioritized list of next actions for near-term execution. The output is machine-usable JSON designed to feed dashboards, decision flows, and executive reviews without a manual analyst in the loop.

**Primary value:** automates a senior sales-ops style pipeline analysis in real time.  
**Use cases:** pipeline reviews, executive reporting, and team prioritization.

---

## Backend Workflow

**Step 1 — HubSpot connection** `Input: Live CRM deal data`
Authenticates against HubSpot CRM v3 APIs. Pulls active deals, stages, dates, values, and core pipeline metadata. Collects the working dataset required for sales analysis.

**Step 2 — Normalization layer** `Intermediate: Clean pipeline dataset`
Standardizes stage values, dates, and probability context. Highlights stale, overdue, and low-momentum opportunities. Builds structured inputs for forecasting and prioritization.

**Step 3 — Intelligence generation** `Processing: Health scoring + prioritization`
Uses GPT-4o to calculate pipeline health and identify risk patterns. Generates weighted forecast logic and high-priority deal focus. Produces recommended next actions for near-term execution.

**Step 4 — Report delivery** `Output: Pipeline intelligence report`
Packages forecast, risk flags, and priorities into structured output. Returns a machine-usable JSON response for BI and dashboard use. Supports real-time pipeline review without manual analyst work.

---

## Report Contains

| Section | Description |
|---|---|
| Pipeline health score | Overall state of the active deal set |
| Risk flags | Stale, overdue, and low-momentum deals |
| Forecast | Weighted revenue projection by stage |
| Priority action list | Ranked next-best actions for near-term execution |
| Decision support | Clear flags for risk and forecast strength |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Framework | Flask |
| Server | Gunicorn |
| AI Model | OpenAI GPT-4o |
| CRM | HubSpot CRM v3 API |
| Deployment | Google Cloud Run — us-east1 |

---

## Local Development

```bash
git clone https://github.com/HansStewart/pipeline-intelligence-agent.git
cd pipeline-intelligence-agent
pip install -r requirements.txt
cp .env.example .env
# Add OPENAI_API_KEY and HUBSPOT_API_KEY to .env
python main.py
# Open http://localhost:8080
```

---

## Deploy to Google Cloud Run

```bash
gcloud run deploy pipeline-intelligence-agent \
  --source . \
  --region us-east1 \
  --allow-unauthenticated
```

---

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | Yes | Intelligence generation and scoring |
| `HUBSPOT_API_KEY` | Yes | CRM v3 API read access |

---

## Full Agent Ecosystem

| Agent | Repository |
|---|---|
| Website Audit Agent | [github.com/HansStewart/website-audit-agent](https://github.com/HansStewart/website-audit-agent) |
| AI Content Pipeline | [github.com/HansStewart/ai-content-pipeline](https://github.com/HansStewart/ai-content-pipeline) |
| Voice-to-CRM Agent | [github.com/HansStewart/voice-to-crm](https://github.com/HansStewart/voice-to-crm) |
| CRM Automation Agent | [github.com/HansStewart/crm-agent](https://github.com/HansStewart/crm-agent) |
| Multi-Agent BI System | [github.com/HansStewart/multi-agent](https://github.com/HansStewart/multi-agent) |
| AI Data Agent | [github.com/HansStewart/ai-data-agent](https://github.com/HansStewart/ai-data-agent) |
| RAG Document Intelligence | [github.com/HansStewart/rag-agent](https://github.com/HansStewart/rag-agent) |
| AI Architecture | [hansstewart.github.io/ai-architecture](https://hansstewart.github.io/ai-architecture) |

---

**Hans Stewart &nbsp;·&nbsp; Marketing Automation Engineer &nbsp;·&nbsp; [hansstewart.dev](https://hansstewart.dev)**
