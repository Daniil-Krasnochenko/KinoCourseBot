import pymysql
import os
import requests
import pymysql.cursors
import mysql.connector
import requests
from aiogram import Router
from aiogram import Bot, Dispatcher,  F
import time
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from io import BytesIO
from aiogram.types import Message
import urllib.parse
from config import Config, load_config

config: Config = load_config(r"C:\Users\Kras.nyi\Desktop\KinoCourse\.env")
router: Router = Router()

# Инициализируем бот и диспетчер
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

error_masage = "The specified row does not exist."

def connection(config: Config) -> pymysql.connect:
    return pymysql.connect(database=config.db.database, 
                           host=config.db.db_host, 
                           user=config.db.db_user,
                           passwd=config.db.db_password, 
                           port=int(config.db.db_port),
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
con = connection(config)
cursor = con.cursor()


def add_user(message: Message) -> bool:
    
    print(message.message_id, message.from_user.id)
    con = connection(config)
    try:
        with con.cursor() as cursor:
            insert_query = f'INSERT INTO user (`user_id`, `country`, `genre`, `actor`)'\
            f'VALUES({message.from_user.id}, "{message.from_user.first_name}", null, null, null, False);'
            cursor.execute(insert_query)
            con.commit()
        return True
    except Exception as ex:
        print(ex)
        print("Ошибка работы бд")
    finally:
        return False
    
        
def have_user(id: int) -> bool:

    try:
        con = connection(config)
        with con.cursor() as cursor:
            find_user = "SELECT * FROM user"\
            f" WHERE user_id = {id}"
            cursor.execute(find_user)
            result = cursor.fetchone()
            # if a row is returned, the user exists in the database
            if result:
                return True
            else:
                return False
    except Exception as ex:
        print(ex)
        return False



def select_one_user(msg: Message):
    try:
        con = connection(config)
        with con.cursor() as cursor:
            select_user = "SELECT * FROM user"\
            f" WHERE user_id = {msg.from_user.id}"
            cursor.execute(select_user)
            return cursor.fetchone()
    except Exception as ex:
        print(ex)

async def update_user(msg: Message, genre_user: str = None,  country: str = None, actor: str = None):
    try:
        con = connection(config)
        if genre_user is not None:
            with con.cursor() as cursor:
                update = f"UPDATE user SET genre = '{genre_user}', country = '{None}', actor = '{None}' WHERE user_id = {msg.from_user.id}"                    
                cursor.execute(update)
                con.commit()
        if actor is not None:
            with con.cursor() as cursor:
                update = f"UPDATE user SET genre = '{None}', country = '{country}', actor = '{None}' WHERE user_id = {msg.from_user.id}"                    
                cursor.execute(update)
                con.commit() 
        if country is not None:
            with con.cursor() as cursor:
                update = f"UPDATE user SET genre = '{None}', country = '{None}', actor = '{actor}' WHERE user_id = {msg.from_user.id}"                    
                cursor.execute(update)
                con.commit()     
        
    except Exception as ex:
        print(ex)




async def display_random_atributs(msg: Message):
    
    con = connection(config)
    with con.cursor() as cursor:
        try:           

            cursor.execute(f"SELECT genre FROM user WHERE user_id = {msg.from_user.id}")
            genre_user = cursor.fetchone()

            cursor.execute(f"SELECT country FROM user WHERE user_id = {msg.from_user.id}")
            country_user = cursor.fetchone()
            
            cursor.execute(f"SELECT actor FROM user WHERE user_id = {msg.from_user.id}")
            actor_user = cursor.fetchone()

            genre = genre_user['genre']
            country = country_user['country']
            actor = actor_user['actor']

            print( genre, country, actor)

  
            if genre_user is not None:
                query = f"SELECT * FROM movie WHERE genre = '{genre}' ORDER BY RAND() LIMIT 1"
            if country_user is not None:
                query = f"SELECT * FROM movie WHERE country = '{country}' ORDER BY RAND() LIMIT 1"
            if actor is not None:
                query = f"SELECT * FROM movie WHERE actor = '{actor}' ORDER BY RAND() LIMIT 1"
                
                
            cursor.execute(query)
            result = cursor.fetchone()
            con.commit()
         
        except KeyError:
            print("The specified row does not exist.")

    title :str = result['title']
    year :int  = result['year']
    description :str= result['description']

    message = f"{title} ({year})\n\n{description}"
    print(message)
    return message




'''
    try:
        # получение url изображения из MySQL
        image_blob = result['picture']
        if image_blob is not None:
            image = URLInputFile(f'{image_blob}')
            print('Все ок')
        else:
            print('Image blob is None')
    except Exception as ex:
        print(ex)

    

    


    
async def genre_random_atributs(msg: Message):
    
    con = connection(config)
    with con.cursor() as cursor:
        try:

            cursor.execute(f"SELECT genre FROM user WHERE user_id = {msg.from_user.id}")
            genre_user = cursor.fetchone()

            genre = genre_user['genre']

            print(genre)

            query = f" genre = '{genre}' ORDER BY RAND() LIMIT 1"
            cursor.execute(query)
                    
            result = cursor.fetchone()

            query = f"UPDATE user SET find_id = {result['id']} WHERE user_id = {msg.from_user.id}"    
            cursor.execute(query)
            con.commit()
                    

        except KeyError:
            print(error_masage)

    title :str = result['title']
    year :int  = result['year']
    description :str= result['description']
    runtime :str= result['runtime']

    message = f"{title} ({year})\n\n{description}\n\nПродолжительность: {runtime}"
    print(message)
    
    return  message

async def country_random_atributs(msg: Message):
    
    con = connection(config)
    with con.cursor() as cursor:
        try:

            cursor.execute(f"SELECT country FROM user WHERE user_id = {msg.from_user.id}")
            country_user = cursor.fetchone()

            country = country_user['country']

            print(country)

            query = f" country = '{country}' ORDER BY RAND() LIMIT 1"
            cursor.execute(query)
                    
            result = cursor.fetchone()

            query = f"UPDATE user SET find_id = {result['id']} WHERE user_id = {msg.from_user.id}"    
            cursor.execute(query)
            con.commit()
                    

        except KeyError:
            print(error_masage)

    title :str = result['title']
    year :int  = result['year']
    description :str= result['description']
    runtime :str= result['runtime']

    message = f"{title} ({year})\n\n{description}\n\nПродолжительность: {runtime}"
    print(message)
    
    return  message


async def actor_random_atributs(msg: Message):
    
    con = connection(config)
    with con.cursor() as cursor:
        try:

            cursor.execute(f"SELECT actor FROM user WHERE user_id = {msg.from_user.id}")
            actor_user = cursor.fetchone()

            actor = actor_user['actors']

            print(actor)

            query = f" actor = '{actor}' ORDER BY RAND() LIMIT 1"
            cursor.execute(query)
                    
            result = cursor.fetchone()

            query = f"UPDATE user SET find_id = {result['id']} WHERE user_id = {msg.from_user.id}"    
            cursor.execute(query)
            con.commit()
                    

        except KeyError:
            print(error_masage)

    title :str = result['title']
    year :int  = result['year']
    description :str= result['description']
    runtime :str= result['runtime']

    message = f"{title} ({year})\n\n{description}\n\nПродолжительность: {runtime}"
    print(message)
    
    return  message
'''