from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_kb() -> InlineKeyboardMarkup:
    """Get kb for main menu
    """
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Кнопка 1', callback_data='cb_btn_1_main')]
    ])
    
    return ikb
