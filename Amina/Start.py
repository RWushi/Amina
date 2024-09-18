import os
from aiohttp import web
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
from Config import bot, dp, app

from Languages import rl
from Menu import rm
from Back import rb
from Questions import rq

dp.include_routers(rl, rm, rb, rq)

async def on_startup(app):
    await bot.set_webhook(os.getenv("WEBHOOK_URL"))


async def on_shutdown(app):
    await bot.delete_webhook()

SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path='/')
app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

if __name__ == '__main__':
    web.run_app(app, port=8080)
