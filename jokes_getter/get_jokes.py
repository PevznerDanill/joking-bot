from os import getenv
import httpx
import asyncio


JOKES_API = getenv("JOKES_API", "https://icanhazdadjoke.com/")


async def get_random_text_joke():
    async with httpx.AsyncClient() as client:
        response = await client.get(JOKES_API, headers={"Accept": "application/json"})
        if response.status_code == 200:
            json_response = response.json()
            return json_response.get("joke")


# asyncio.run(get_random_joke())