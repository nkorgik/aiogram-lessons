import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from const import TOKEN_API


bot = Bot(token=TOKEN_API)
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(msg: types.Message) -> None:
    """Handles command start"""

    await msg.answer('Hello World!')


async def main():
    """Entry point"""

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())






