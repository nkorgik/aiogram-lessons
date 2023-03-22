import logging 

from aiogram import Bot, Dispatcher, types
from aiohttp import web 
from config import TOKEN_API

ADMIN_ID = "6018428620" # this can be str or int

bot = Bot(token=TOKEN_API)
Bot.set_current(bot) # in some cases you might get exception that your current bot instance is not defined so this will solve your problem
dp = Dispatcher(bot)
app = web.Application() # that's our web-server AIOHTTP for handling concurrent requests from ngrok-Telegram API

webhook_path = f'/{TOKEN_API}' # this is the path for your TOKEN_API 'URI'


async def set_webhook():
    webhook_uri = f'https://925e-180-232-84-202.ap.ngrok.io{webhook_path}'
    await bot.set_webhook(
        webhook_uri # here we are telling our Telegram API to use the WEBHOOK
    )
    
async def on_startup(_):
    await set_webhook()
    await bot.send_message(chat_id=ADMIN_ID, text='Bot has been started')


async def on_shutdown(_):
    await bot.send_message(chat_id=ADMIN_ID, text='Bot has been stopped')


@dp.message_handler(commands=['start', 'help'])
async def cmd_start_help(message: types.Message) -> None:
    await message.answer('Hello, welcome to our webhook bot!')
    
    
async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind('/')
    token = url[index+1:] # this method is used because in some cases request object can't be correctly interpreted and match_info will return empty object
    if token == TOKEN_API:
        update = types.Update(**await request.json()) # we just parse our bytes into dictionary
        await dp.process_update(update) # this will just process update using the appropriate handler
        return web.Response() # construct the response object
    else:
        return web.Response(status=403) # if our TOKEN is not authenticated
    
app.router.add_post(f'/{TOKEN_API}', handle_webhook) # here we set router for process each webhook http request through our handler_


if __name__ == "__main__":
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    
    web.run_app(
        app, 
        host='0.0.0.0', 
        port=8000
    )
    