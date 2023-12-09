import asyncio 

from aiogram import Dispatcher

from bot_instance import bot
from bot.handlers.user_handlers import user_router
from bot.config import BotConfig


def register_routers(dp: Dispatcher) -> None:
    """Registers routers"""

    dp.include_router(user_router)


async def main() -> None:
    """The main function which will execute our event loop and start polling."""
    
    config = BotConfig(admin_ids=[123456, 6018428620], welcome_message="Welcome to our Python Bot!")
    dp = Dispatcher()
    dp["config"] = config

    register_routers(dp)
    
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
