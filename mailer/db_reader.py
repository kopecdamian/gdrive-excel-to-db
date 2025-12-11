import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

# Save all retrieved data into the database table
def load_from_db():
    # open connection with database
    conn = psycopg2.connect(
        host=os.getenv('PSQL_HOST'), 
        port=5432,
        dbname=os.getenv('DB_NAME'), 
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )
    cur = conn.cursor()

    cur.execute("SELECT product, company, TO_CHAR(purchase_date, 'YYYY-MM-DD') FROM purchases WHERE (purchase_date + INTERVAL '20 months') <= CURRENT_DATE AND (purchase_date + INTERVAL '24 months') >= CURRENT_DATE ORDER BY purchase_date DESC;")
    rows = cur.fetchall()
    
    # close connection with database
    cur.close()
    conn.close()

    receipts_list = ''
    for i, row in enumerate(rows, start=1):
        product, company, purchase_date = row
        receipts_list+=f"{i}. {product} — {company} — {purchase_date}<br>"

    if receipts_list == '':
        receipts_list = 'Brak rzeczy'
    return(receipts_list)

load_from_db()
