import asyncio
import datetime

from aioscheduler import TimedScheduler
from aiogram import types, Dispatcher, Bot, exceptions


TOKEN_API = "5871111612:AAFWkjY3_cQazaJNkbDghDigX-mjdKSbArA"


async def some_work() -> None:
    print('Hello My Friend!')


async def cmd_start(msg: types.Message) -> None:
    try:
        run_time = datetime.datetime.now() + datetime.timedelta(seconds=7)
        await ascheduled_msg(msg, run_time)
    except exceptions.BotBlocked:
        print(f"Bot is blocked by the user with id: {msg.from_user.id}")
    except exceptions.ChatNotFound:
        print(f"Chat not found for user with id: {msg.from_user.id}")


async def ascheduled_msg(run_time) -> None:
    scheduler = TimedScheduler()
    scheduler.start()
    
    scheduler.schedule(coro=some_work(), when=run_time)


async def main():
    bot = Bot(TOKEN_API)
    dp = Dispatcher(bot)
    
    dp.register_message_handler(cmd_start, commands=['start'])
    task = asyncio.create_task(ascheduled_msg(datetime.timedelta(seconds=2)))
    try:
        await asyncio.gather(dp.start_polling(), task)
    except Exception as _ex:
        print(_ex)
    finally:
        _session = await bot.get_session() 
        # Hate `aiohttp` devs because it juggles event-loops and breaks already opened session =D
        await _session.close()
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, ConnectionError):
        pass
    