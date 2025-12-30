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

# Requirements
- Docker
- Docker-compose
- Python 3.11+
- AWS account with SES
- Google account with API access to Drive
- Configure .env

# Installation and run
git clone https://github.com/kopecdamian/gdrive-excel-to-db.git
cd gdrive-excel-to-db
docker-compose build
docker-compose run --rm data_loader
docker-compose run --rm mailer
