import os
import requests
from dotenv import load_dotenv

load_dotenv()

HUBSPOT_TOKEN = os.getenv("HUBSPOT_TOKEN")
BASE_URL = "https://api.hubapi.com"

HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_TOKEN}",
    "Content-Type": "application/json"
}

def get_all_deals():
    url = f"{BASE_URL}/crm/v3/objects/deals"
    params = {
        "limit": 100,
        "properties": "dealname,amount,dealstage,closedate,hubspot_owner_id,hs_deal_stage_probability,createdate,notes_last_updated,num_contacted_notes,hs_next_step"
    }
    all_deals = []

    while url:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()
        all_deals.extend(data.get("results", []))
        paging = data.get("paging", {})
        next_page = paging.get("next", {}).get("link")
        url = next_page
        params = {}

    return all_deals

def get_pipeline_stages():
    url = f"{BASE_URL}/crm/v3/pipelines/deals"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get("results", [])