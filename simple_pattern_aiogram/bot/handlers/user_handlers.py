from aiogram import types, Dispatcher

from bot.keyboards.user_keyboards import get_main_kb


async def cmd_start(msg: types.Message) -> None:
    """Command start

    Args:
        msg (types.Message): msg object
    """
    reply_text = 'Привет, как твои дела?\n'
    reply_text += f'Твое имя - {msg.from_user.first_name}!'
    
    await msg.answer(
        text=reply_text,
        reply_markup=get_main_kb()
    )


def register_user_handlers(dp: Dispatcher) -> None:
    """Register user handlers
    """

    dp.register_message_handler(cmd_start, commands=['start'])
