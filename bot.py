import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = config.bot_token.get_secret_value()

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    print(message.from_user.username)
    await message.answer("Hi")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
