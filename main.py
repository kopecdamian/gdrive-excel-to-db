from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv
import os
import psycopg2

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

# Save all retrieved data into the database table
def save_to_db():
    # open connection with database
    conn = psycopg2.connect(
        host=os.getenv('PSQL_HOST'), 
        port=5432,
        dbname=os.getenv('DB_NAME'), 
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )
    cur = conn.cursor()
    
    all_receipts = get_file()

    # Insert only non-duplicate records into the database table
    for receipt in all_receipts:
        purchase_date = receipt[0]
        product = receipt[1]
        company = receipt[2]
        cur.execute(f"INSERT INTO purchases (product, company, purchase_date) VALUES ('{product}', '{company}', '{purchase_date}') ON CONFLICT DO NOTHING;")

    conn.commit()
    
    # close connection with database
    cur.close()
    conn.close()

save_to_db()
