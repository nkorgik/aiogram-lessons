from aiogram.filters import Command
from aiogram import Router, types 

from bot.config import BotConfig

user_router = Router()


# @user_router.message(Command('start'))
# async def cmd_start(msg: types.Message) -> None:
#     """Process the `start` command"""

#     await msg.answer('Hello <b>World</b>!')


@user_router.message(Command("reply"))
async def cmd_reply(message: types.Message):
    """The function replies to your message"""
    
    await message.reply('Reply message replies! 😻')


@user_router.message(Command("dice"))
async def cmd_dice(message: types.Message):
    """The function answers dice to your message"""
    
    await message.answer_dice(emoji="🎲")


@user_router.message(Command("admin_info"))
async def cmd_admin_info(message: types.Message, config: BotConfig):
    if message.from_user.id in config.admin_ids:
        await message.answer("You are an admin.")
    else:
        await message.answer("You are not an admin.")


@user_router.message(Command("start"))
async def cmd_start(message: types.Message, config: BotConfig):
    await message.answer(config.welcome_message)

