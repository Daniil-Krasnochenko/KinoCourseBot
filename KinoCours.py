from typing import Literal
from dataclasses import dataclass
import os
import psycopg2
import telebot

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

bot = telebot.TeleBot('your_bot_token')
#Actor : dict[Literal['name'] | Literal['last_name'] | Literal['fullname'], str]
"""
@dataclass
class Actor:
    name: str
    last_name: str
    fullname: str = name + " " + last_name
"""
"""
@dataclass
class DatabaseConfig:
    db_host: str       # URL-адрес базы данных
    db_user: str       # Username пользователя базы данных
    db_password: str   # Пароль к базе данных
    database: str      # Название базы данных


@dataclass
class TgBot:
    token: str             # Токен для доступа к телеграм-боту
    admin_ids: list[int]   # Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
    
"""
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello, World!')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (message_text) VALUES (%s)", (message.text,))
    conn.commit()
    bot.reply_to(message, message.text)

bot.infinity_polling()
