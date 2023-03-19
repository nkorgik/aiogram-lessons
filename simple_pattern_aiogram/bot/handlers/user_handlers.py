from aiogram import types, Dispatcher


async def cmd_start(msg: types.Message) -> None:
    await msg.answer(
        text='Hello world',
    )
    
    
async def cmd_help(msg: types.Message) -> None:
    await msg.answer(
        text='HELP COMMAND',
    )
    
    
def register_user_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(cmd_start, commands=['start'])    
    dp.register_message_handler(cmd_help, commands=['help'])    

    # callback handlers, message handlers
    
    