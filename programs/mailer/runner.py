from db_reader import load_from_db
from email_sender import send_email
send_email(load_from_db())
