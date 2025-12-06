import os
import psycopg2

# Save all retrieved data into the database table
def save_to_db(data):
    # open connection with database
    conn = psycopg2.connect(
        host=os.getenv('PSQL_HOST'), 
        port=5432,
        dbname=os.getenv('DB_NAME'), 
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASS')
    )
    cur = conn.cursor()
    
    all_receipts = data

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
