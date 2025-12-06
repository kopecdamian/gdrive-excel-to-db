import boto3
from dotenv import load_dotenv
import os

load_dotenv()

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
                'Data': 'This message body contains HTML formatting. It can, for example, contain links like this one: <a class="ulink" href="http://docs.aws.amazon.com/ses/latest/DeveloperGuide" target="_blank">Amazon SES Developer Guide</a>.',
            },
            'Text': {
                'Charset': 'UTF-8',
                'Data': 'This is the message body in text format.',
            },
        },
        'Subject': {
            'Charset': 'UTF-8',
            'Data': 'Test email',
        },
    },
    Source=os.getenv('SENDER_EMAIL')
)

print(response)
