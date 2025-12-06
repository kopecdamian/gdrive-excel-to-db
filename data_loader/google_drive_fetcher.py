from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive"]
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

# Authorization for Google Drive
def authenticate():
    creds = Credentials.from_service_account_file(os.getenv('SERVICE_ACCOUNT_FILE'), scopes = SCOPES)
    return creds

# Get Excel file content from Google Drive
def get_file():
    creds = authenticate()
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range="A2:Z",
    ).execute()['values']
    return(result)
