import requests
import os
import django

from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()
from bot_settings.models import Sentence, BotUser

TOKEN = os.getenv("TOKEN")
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def get_all_sentences():
    result = ""
    sentences = list(Sentence.objects.all())
    for sentence in sentences:
        if sentence:
            formatted_message = (
                f"Message: {sentence.message}\n"
                f"Author: {sentence.author}\n"
                f"Created At: {sentence.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
            )
            result += '\n\n\n' + formatted_message
    return result

def get_all_users():
    return list(BotUser.objects.all())

def send_task():
    users = get_all_users()
    text = get_all_sentences()
    for user in users:
        chat_id = user.chat_id

        payload = {
            "chat_id": chat_id,
            "text": text
        }
        requests.post(url, data=payload)

# send_task()