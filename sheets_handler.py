import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def connect_to_sheets(sheet_name):
    creds_path = os.getenv("GOOGLE_CREDENTIALS_PATH")
    if not creds_path:
        raise Exception("GOOGLE_CREDENTIALS_PATH not set in environment variables.")
    
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet
