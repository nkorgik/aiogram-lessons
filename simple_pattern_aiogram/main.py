import asyncio
import os
# import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types

from bot.handlers.user_handlers import register_user_handlers


def register_handler(dp: Dispatcher) -> None:
    register_user_handlers(dp)


async def main() -> None:
    """Entry point
    """
    load_dotenv('.env')
    
    token = os.getenv("TOKEN_API")
    bot = Bot(token)
    dp = Dispatcher(bot)
    
    register_handler(dp)
    
    try: 
        await dp.start_polling()
    except Exception as _ex:
        print(f'There is an exception - {_ex}')


if __name__ == "__main__":
    asyncio.run(main())
