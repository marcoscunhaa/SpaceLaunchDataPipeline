import os
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

credentials_path = os.path.join(BASE_DIR, os.getenv("GOOGLE_CREDENTIALS_PATH"))

print("Credenciais em:", credentials_path)

creds = Credentials.from_service_account_file(
    credentials_path,
    scopes=SCOPES
)

client = gspread.authorize(creds)

def get_sheet(sheet_name):
    return client.open(sheet_name).sheet1