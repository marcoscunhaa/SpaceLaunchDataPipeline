import pandas as pd

def process_launch_data(data):
    launches = []
    if not data or not data.get("results"):
        return pd.DataFrame()

    for launch in data["results"]:
        lsp = launch.get("launch_service_provider") or {}

        launches.append({
            "id": str(launch.get("id")),
            "name": str(launch.get("name")),
            "provider": str(lsp.get("name")),
            "launch_date": launch.get("net"),
            "status": str(launch.get("status", {}).get("name")),
            "location_name": str(launch.get("pad", {}).get("location", {}).get("name")),
            "country": str(launch.get("pad", {}).get("location", {}).get("country_code")),
            "rocket_name": str(launch.get("rocket", {}).get("configuration", {}).get("name")),
            "mission_type": str(launch.get("mission", {}).get("type") if launch.get("mission") else "N/A"),
            "orbit": str(launch.get("mission", {}).get("orbit", {}).get("name") if launch.get("mission") and isinstance(
                launch.get("mission").get("orbit"), dict) else "N/A")
        })

    df = pd.DataFrame(launches)

    df["launch_date"] = pd.to_datetime(df["launch_date"], errors="coerce", utc=True)
    df = df.sort_values(by="launch_date", ascending=False)
    df = df.head(200)

    df["launch_date_str"] = df["launch_date"].dt.strftime("%m/%d/%Y %H:%M")
    df["launch_year"] = df["launch_date"].dt.year.fillna(0).astype(int)
    df["launch_month"] = df["launch_date"].dt.month.fillna(0).astype(int)

    cols = ["id", "name", "provider", "launch_date_str", "launch_year", "launch_month", "status", "location_name",
            "country", "rocket_name", "mission_type", "orbit"]

    final_df = df.reindex(columns=cols).fillna("").astype(str).replace(["nan", "NaN", "None", "NaT"], "")

    return final_df