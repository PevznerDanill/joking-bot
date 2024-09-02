from jokes_getter import get_random_text_joke


async def default_joke_sender(bot, chat_id):
    message = await get_random_text_joke()
    if message:
        await bot.send_message(chat_id=chat_id, text=message)