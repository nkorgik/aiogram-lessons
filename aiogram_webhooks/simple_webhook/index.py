from aiohttp import web

from aiogram import Bot, Dispatcher, types

from config import TOKEN_API


bot = Bot(token=TOKEN_API)
Bot.set_current(bot)
dp = Dispatcher(bot)

app = web.Application()

webhook_path = f'/{TOKEN_API}'

async def set_webhook():
    webhook_uri = f'https://c3a4-180-232-84-202.ap.ngrok.io{webhook_path}'
    await bot.set_webhook(
        webhook_uri
    )
    

async def on_startup(_):
    await set_webhook()
    

@dp.message_handler(commands=['start', 'help'])
async def cmd_start_help(msg: types.Message) -> None:
    await msg.answer('Hello World!')
    
    
async def handle_webhook(request):
    url = str(request.url)
    index = url.rfind('/')
    token = url[index+1:]
    
    if token == TOKEN_API:
        update = types.Update(**await request.json())
        await dp.process_update(update)
        
        return web.Response()
    else:
        return web.Response(status=403)


app.router.add_post(f'/{TOKEN_API}', handler=handle_webhook)


if __name__ == "__main__":
    app.on_startup.append(on_startup)
    
    web.run_app(
        app,
        host='0.0.0.0',
        port='8080'
    )
