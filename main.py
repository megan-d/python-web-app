from typing import Union

from fastapi import FastAPI
import httpx
import os
import asyncio

app = FastAPI()

# api_key = os.environ["ENV_KEY"]

URL = f'https://api.polygon.io/v1/open-close/AAPL/2024-12-20?adjusted=true&apiKey='

async def request(client):
    response: httpx.Response = await client.get(URL)
    return response


async def get_daily_open_close():
    async with httpx.AsyncClient() as client:
        result = await request(client)
        result_json = result.json()
        return result_json

@app.get("/")
async def read_root():
    result = await get_daily_open_close()
    return result