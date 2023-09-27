import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from aiogram.utils.markdown import hbold

from token_api import TOKEN_API


dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    """Process the command `start`"""
    
    reply_text = f'Hello, {hbold(msg.from_user.first_name)}'
    
    await msg.answer(
        text=reply_text
    )


async def main() -> None:
    """Entry Point"""
    
    bot = Bot(
        token=TOKEN_API,
        parse_mode='HTML'
    )
    
    await dp.start_polling(bot)



if __name__ == '__main__':

    asyncio.run(main())



