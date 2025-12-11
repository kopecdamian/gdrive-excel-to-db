import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(message='test'):
    ses_client = boto3.client(
        'ses'
    )

    response = ses_client.send_email(
        Destination={
            'ToAddresses': [
                os.getenv('RECIPIENT_EMAIL')
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': message,
                    }
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Podsumowanie paragonow',
            },
        },
        Source=os.getenv('SENDER_EMAIL')
    )

    print(response)
