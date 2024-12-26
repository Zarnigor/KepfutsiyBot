import asyncio
import logging
import sys
import os
import django

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.filters import Command

from asgiref.sync import sync_to_async
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()

from bot_settings.models import Sentence

from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@sync_to_async
def get_all_sentences():
    return list(Sentence.objects.all())

@dp.message(Command('send_sentence'))
async def send_sentence(message: Message):
    try:
        result = ""
        sentences =  await get_all_sentences()
        for sentence in sentences:
            if sentence:
                formatted_message = (
                    f"Message: {sentence.message}\n"
                    f"Author: {sentence.author}\n"
                    f"Created At: {sentence.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
                )
                result += '\n\n\n' + formatted_message

        if result != "":
            await message.answer(result)
        else:
            await message.answer("No sentences found in the database.")
    except Exception as e:
        await message.answer(f"An error occurred: {e}")


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())