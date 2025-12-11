# gdrive-excel-to-db
This application automates the processing of purchase data retrieved from an Excel file stored on Google Drive and sending summarized reports via email.
The system operates in two main steps:
1. Data Import:
- Downloads an Excel file from Google Drive.
- Inserts the extracted data into a PostgreSQL database.
- Skips duplicate entries using ON CONFLICT DO NOTHING.
2. Summary Generation and Email Delivery:
- Reads stored records from PostgreSQL.
- Formats the data into an HTML summary.
- Sends the report via AWS SES.

# Installation
git clone https://github.com/kopecdamian/get-receipts.git
pip install -r requirements.txt
