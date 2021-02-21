import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv("ACC_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)


class NotificationManager:

    def __init__(self):
        self.message = None

    def send_sms(self, msg):
        self.message = client.messages.create(
            from_='+13343676244',
            body=msg,
            to=os.getenv("MY_PHONE")
        )

        print(self.message.status)
    pass
