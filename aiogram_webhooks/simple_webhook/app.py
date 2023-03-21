import logging
from aiogram import Bot, Dispatcher, types
from aiohttp import web

API_TOKEN = '5871111612:AAFcEYpGC8EmUCTQgoOaiKw_4CipE0h0pz4'


admin_id = 6018428620

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
Bot.set_current(bot)
dp = Dispatcher(bot)
app = web.Application()


webhook_path = f'/{API_TOKEN}'

async def set_webhook():
    webhook_url = f'https://2ff7-180-232-84-202.ap.ngrok.io{webhook_path}'
    await bot.set_webhook(webhook_url)


async def on_startup(dp):
    await set_webhook()
    await bot.send_message(chat_id=admin_id, text='Bot has been started')


async def on_shutdown(dp):
    await bot.send_message(chat_id=admin_id, text='Bot has been stopped')


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! I'm your webhook-enabled Telegram bot!")


async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind('/')
    token = url[url.rfind('/')+1:]

    if token == API_TOKEN:
        update = types.Update(**await request.json())
        await dp.process_update(update)
        return web.Response()
    else:
        return web.Response(status=403)


app.router.add_post(f'/{API_TOKEN}', handle_webhook)


if __name__ == '__main__':
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    
    web.run_app(
        app,
        host='0.0.0.0',  # Listen on all available network interfaces
        port=8000  # You can change the port if needed
    )
