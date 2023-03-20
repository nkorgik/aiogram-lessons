import os 
import logging 
import sqlite3 

from aiogram import Bot, Dispatcher, types, executor
from dotenv import load_dotenv # import dotenv

load_dotenv()
api_token = os.getenv('TOKEN_API') # API token for API requests


bot = Bot(token=api_token) # bot instance
dp = Dispatcher(bot) # Dispatcher for API requests


@dp.message_handler(commands=['start']) # Start the bot
async def send_welcome(message: types.Message) -> None:
    """Send welcome message

    Args:
        message (types.Message): Received Message object
    """
    await message.answer('Привет! Я бот для работы с базой данных.')


def create_users_table(): # Create users table
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL DEFAULT 'email@example.com'
    )''')
    conn.commit()
    conn.close()

create_users_table()



@dp.message_handler(commands=['add']) # add commands
async def cmd_add(message: types.Message) -> None:
    """Just adds current user who wrote /add

    Args:
        message (types.Message): _description_
    """
    user_id = message.from_user.id
    
    if message.from_user.username:
        username = message.from_user.username 
    else:
        username = message.from_user.first_name
    
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users (id, name) VALUES (?,?)''', (user_id, username,))
    
    conn.commit()
    conn.close()
    
    await message.reply(f'Пользователь был создан с данными - USERNAME: {username} && ID: {user_id}')
    

@dp.message_handler(commands=['list',])
async def cmd_list(message: types.Message):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    users = c.fetchall()
    conn.close()
    
    await message.reply(f'Список пользователей: {users}')


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        filemode='w',
        filename='logs.txt',
    )
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
