import os
import sys

from dotenv import load_dotenv

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from api_client import fetch_space_race_data
from data_processing import process_launch_data
from sheets_client import get_sheet

load_dotenv()


def main():
    try:
        print("✔️ Starting spatial data extraction")

        # 1. Extração
        data = fetch_space_race_data()

        # 2. Processamento
        df = process_launch_data(data)

        if df.empty:
            print("❌ Error: No data processed.")
            return

        # 3. Configuração do Sheets
        sheet = get_sheet(os.getenv("SHEET_NAME"))
        sheet.clear()

        # 4. Gravação do Cabeçalho
        print("✔️ Writing header")

        header = df.columns.tolist()
        rows = df.values.tolist()

        full_data = [header] + rows

        print(f"🚀 Uploading {len(rows)} rows to Google Sheets...")
        sheet.update('A1', full_data)

        print(f"\n✅ Success!")

    except Exception as e:
        print(f"❌ General Failure: {e}")


if __name__ == "__main__":
    main()