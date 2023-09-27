import asyncio

from token_api import TOKEN_API
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command


dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(msg: types.Message) -> None:
    await msg.answer(
        text='Hello World!'
    )

async def cmd_answer(message: types.Message):
    await message.answer("This is a simple answer! ❤️‍🩹")


dp.message.register(cmd_answer, Command("answer"))

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="")


async def main() -> None:
    bot = Bot(TOKEN_API)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

