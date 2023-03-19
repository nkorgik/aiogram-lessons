import asyncio 
import os 
import logging 

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

# handlers
from bot.handlers.user_handlers import register_user_handlers


def register_handlers(dp):
    register_user_handlers(dp)
    # register handlers - admin, client, products 


async def main():
    load_dotenv() # load environment variables
    token = os.environ.get('TOKEN_API') # take token from environment variable
    
    bot = Bot(token) # create bot instance
    dp = Dispatcher(bot) # create dispatcher instance
    
    register_handlers(dp) # register all handlers
    
    try:
        await dp.start_polling() # start polling
    except Exception as _ex:
        logging.error(_ex) 



if __name__ == '__main__':
    fmt='%(asctime)s:%(message)s'
    
    logging.basicConfig(
        format=fmt,
        level=logging.INFO,
        filemode='w',
        filename='logs.txt'
    )
    
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info('Bot has been terminated successfully!')
