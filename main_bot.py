import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from sender import default_joke_sender



async def main():
    load_dotenv()
    token = getenv("BOT_TOKEN")
    chat_id = getenv("CHAT_ID")


    async with Bot(
        token=token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    ) as bot:
        await default_joke_sender(chat_id=chat_id, bot=bot)


if __name__ == "__main__":
    asyncio.run(main())