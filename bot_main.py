import telebot
import os
import django

from dotenv import load_dotenv


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()
from bot_settings.models import BotUser

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"), parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	BotUser.objects.create(chat_id=message.chat.id, first_name=message.chat.first_name, username=message.chat.username)
	bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()

