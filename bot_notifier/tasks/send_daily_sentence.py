import requests
import os

from dotenv import load_dotenv
load_dotenv()

from bot_notifier.models import BotUser, Sentence

TOKEN = os.getenv("TOKEN")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def get_all_users():
    return list(BotUser.objects.all())

def send_task():
    users = get_all_users()
    text = Sentence.objects.order_by('?').first().message
    for user in users:
        chat_id = user.chat_id

        payload = {
            "chat_id": chat_id,
            "text": text
        }
        requests.post(url, data=payload)
