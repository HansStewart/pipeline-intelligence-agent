🧠 Pipeline Intelligence Agent

> An AI-powered sales operations agent that connects directly to HubSpot, pulls live deal data, and returns a full pipeline intelligence report — built with Python, GPT-4o, and deployed on Google Cloud Run.



📌 Overview

The Pipeline Intelligence Agent is a production-ready AI agent that automates the work of a senior sales operations analyst. It retrieves all active deals from your HubSpot CRM, processes the data through GPT-4o, and generates a comprehensive intelligence report — surfacing deals at risk, prioritized actions, revenue forecasts, and pipeline health scores in real time.



]🚀 Features

- Live HubSpot Integration — Pulls all active deals and pipeline stage data via the HubSpot CRM v3 API
- GPT-4o Analysis Engine — Sends structured deal data to GPT-4o for deep sales intelligence analysis
- Pipeline Health Score — Scores your pipeline 0–100 with a clear explanation
- Revenue Forecast Summary — Total pipeline value, weighted forecast, and deals closing this month
- Deals to Prioritize This Week — Top 3–5 deals ranked by urgency with specific reasoning
- Deals at Risk — Flags stale deals, overdue close dates, and low-probability opportunities
- Recommended Next Actions — Specific, actionable next steps per deal
- Overall Pipeline Observations** — Trend analysis and pattern detection across the full pipeline
- Health Check Endpoint — `/health` route for uptime monitoring and deployment verification
- Cloud-Native Deployment — Containerized with Docker and deployed on Google Cloud Run



🛠 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| Web Framework | Flask 3.0.3 |
| AI Engine | OpenAI GPT-4o |
| CRM Integration | HubSpot CRM API v3 |
| HTTP Client | Requests 2.32.3 |
| Environment Config | python-dotenv |
| Production Server | Gunicorn |
| Containerization | Docker |
| Cloud Deployment | Google Cloud Run |
| CI/CD | Google Cloud Build |



📁 Project Structure

```
pipeline-intelligence-agent/
├── app.py                  # Flask app — routes and HTML report wrapper
├── hubspot_client.py       # HubSpot API client — fetches deals and pipeline stages
├── analyzer.py             # GPT-4o analysis engine — generates the intelligence report
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
├── .dockerignore           # Files excluded from Docker build
├── .env                    # Local environment variables (never committed)
├── .env.example            # Environment variable template for contributors
└── .gitignore              # Git exclusions
```



⚙️ Setup & Installation

Prerequisites

- Python 3.11+
- Git
- Docker (for containerized deployment)
- Google Cloud SDK (for Cloud Run deployment)
- HubSpot account with Private App access
- OpenAI API key

1. Clone the Repository

```bash
git clone https://github.com/HansStewart/pipeline-intelligence-agent.git
cd pipeline-intelligence-agent
```

2. Create a Virtual Environment

```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
source venv/bin/activate        # macOS / Linux
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Configure Environment Variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Open `.env` and set your values:

```env
OPENAI_API_KEY=your_openai_api_key_here
HUBSPOT_TOKEN=your_hubspot_private_app_token_here
```

5. HubSpot Private App Setup

This agent requires a HubSpot Private App token with the following scopes:

- `crm.objects.deals.read`
- `crm.schemas.deals.read`
- `crm.pipelines.orders.read`

To generate a token:
1. Go to HubSpot Settings → Integrations → Private Apps
2. Click Create a private app
3. Under the Scopes tab, enable the three scopes above
4. Click Create app and copy the `pat-` token



▶️ Running Locally

```bash
python app.py
```

Open your browser and navigate to:

```
http://localhost:8080
```

The report will generate in **15–30 seconds** as the agent fetches your live HubSpot data and runs it through GPT-4o.

***

## 🐳 Running with Docker

```bash
docker build -t pipeline-intelligence-agent .
docker run -p 8080:8080 --env-file .env pipeline-intelligence-agent
```



☁️ Deploying to Google Cloud Run

Deploy from Source

```bash
gcloud run deploy pipeline-intelligence-agent \
  --source . \
  --region us-central1 \
  --platform managed \
  --allow-unauthenticated \
  --timeout 120
```

Set Environment Variables

```bash
gcloud run services update pipeline-intelligence-agent \
  --region us-central1 \
  --set-env-vars OPENAI_API_KEY=your_key_here,HUBSPOT_TOKEN=your_token_here
```



🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Generates and returns the full pipeline intelligence report |
| `GET` | `/health` | Returns agent status for uptime monitoring |

Health Check Response

```json
{
  "status": "ok",
  "agent": "pipeline-intelligence-agent"
}
```



📊 Report Sections

The generated report includes the following sections:

1. Pipeline Health Score — A 0–100 score with a written explanation of what is driving the number
2. Revenue Forecast Summary — Total pipeline value, probability-weighted forecast, and this month's closeable deals
3. Deals to Prioritize This Week — Ranked list with the reasoning behind each prioritization
4. Deals at Risk — Flags deals with no recent activity, overdue close dates, or low win probability
5. Recommended Next Actions — Specific, deal-level action items for your sales team
6. Overall Observations — Pattern analysis and strategic commentary on the state of the pipeline



🔐 Security Notes

- Never commit your `.env` file — it is excluded via `.gitignore`
- Use Google Cloud Secret Manager for production-grade secret management
- The HubSpot token used is a read-only Private App token — it cannot modify your CRM data
- Cloud Run services can be restricted to authenticated access by removing `--allow-unauthenticated`



🗺 Roadmap

- [ ] Add Slack notification integration to post daily reports automatically
- [ ] Add deal-level trend tracking across multiple report generations
- [ ] Support multiple HubSpot pipelines with a dropdown selector
- [ ] Add a PDF export option for the intelligence report
- [ ] Integrate with Google Sheets for persistent pipeline tracking




👤 Author

Hans Stewart
[GitHub](https://github.com/HansStewart)



Built with Python, OpenAI, HubSpot API, and Google Cloud Run.