import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_pipeline(deals, stages):
    deals_summary = []
    for deal in deals:
        props = deal.get("properties", {})
        deals_summary.append({
            "id": deal.get("id"),
            "name": props.get("dealname", "Unnamed Deal"),
            "amount": props.get("amount", "0"),
            "stage": props.get("dealstage", "unknown"),
            "close_date": props.get("closedate", "Not set"),
            "probability": props.get("hs_deal_stage_probability", "unknown"),
            "last_activity": props.get("notes_last_updated", "None"),
            "contacts_made": props.get("num_contacted_notes", "0"),
            "next_step": props.get("hs_next_step", "Not set")
        })

    stage_names = {}
    for pipeline in stages:
        for stage in pipeline.get("stages", []):
            stage_names[stage["id"]] = stage["label"]

    for deal in deals_summary:
        stage_id = deal["stage"]
        deal["stage_label"] = stage_names.get(stage_id, stage_id)

    prompt = f"""
You are a senior sales operations analyst. Analyze the following HubSpot pipeline data and return a full intelligence report in clean HTML format.

Pipeline Data:
{json.dumps(deals_summary, indent=2)}

Your report must include ALL of the following sections:

1. Pipeline Health Score (0-100 with a brief explanation)
2. Revenue Forecast Summary (total pipeline value, weighted forecast, deals closing this month)
3. Deals to Prioritize This Week (top 3-5 deals with reason why)
4. Deals at Risk (flag deals with no recent activity, past close dates, or low probability - explain each)
5. Recommended Next Actions (per deal - be specific and actionable)
6. Overall Observations (1-2 paragraphs on pipeline trends and patterns)

Format everything as clean, readable HTML with proper headings, tables where appropriate, and bullet points. Use inline styles sparingly for emphasis. Be direct and specific - no filler language.
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a world-class sales operations analyst. Return only clean, well-structured HTML."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content