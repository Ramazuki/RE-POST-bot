import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import commands, posts, secretmodule

logging.basicConfig(level=logging.INFO)


async def main():
    BOT_TOKEN = config.bot_token.get_secret_value()
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(posts.router, secretmodule.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
