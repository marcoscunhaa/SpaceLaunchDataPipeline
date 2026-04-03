import requests
import time
from datetime import datetime, timezone

BASE_URL = "https://ll.thespacedevs.com/2.2.0/launch/"


def fetch_with_retry(url, max_retries=3):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 429:
                wait_time = (attempt + 1) * 30
                print(f"⚠️ Rate limit reached. Awaiting response: {wait_time}s...")
                time.sleep(wait_time)
                continue
            response.raise_for_status()
            return response.json()
        except Exception as e:
            if attempt == max_retries - 1: return None
            time.sleep(5)
    return None


def fetch_space_race_data():
    agencies = [44, 121]
    all_launches = []
    now_iso = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

    for agency_id in agencies:
        url = f"{BASE_URL}?lsp__id={agency_id}&limit=100&ordering=-net&net__lte={now_iso}"

        data = fetch_with_retry(url)

        if data and "results" in data:
            all_launches.extend(data["results"])
            print(f"✔️ Agency {agency_id}: {len(data['results'])} releases found.")
        else:
            print(f"❌ Agency failure {agency_id}.")

        if agency_id != agencies[-1]:
            print("✔️ Waiting 30 seconds to avoid blocking")
            time.sleep(30)

    return {"results": all_launches}