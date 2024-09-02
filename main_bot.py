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
    chat_id = getenv("TEST_CHAT_ID")
    frequency = int(getenv("FREQUENCY"))

    async with Bot(
        token=token,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    ) as bot:
        while True:
            await default_joke_sender(chat_id=chat_id, bot=bot)
            await asyncio.sleep(frequency)


if __name__ == "__main__":
    asyncio.run(main())