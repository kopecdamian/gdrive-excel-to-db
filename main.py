from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive"]
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

def authenticate():
    creds = Credentials.from_service_account_file(os.getenv('SERVICE_ACCOUNT_FILE'), scopes = SCOPES)
    return creds

def get_file():
    creds = authenticate()
    service = build('sheets', 'v4', credentials=creds)
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range="A2:Z",
    ).execute()
    print(result['values'])

def save_to_db():
    conn = psycopg2.connect(
        host=os.getenv('PSQL_HOST'), 
        port=5432,
        dbname=os.getenv('DB_NAME'), 
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )
    cur = conn.cursor()

    cur.execute("INSERT INTO purchases (product, company, purchase_date) VALUES ('Kawa', 'Starbucks', '2025-01-12');")

    conn.commit()
            
    cur.close()
    conn.close()
# get_file()

save_to_db()
