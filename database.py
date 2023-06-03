import pymysql
import os
import requests
import pymysql.cursors
import mysql.connector
import requests
from aiogram import Router
from aiogram import Bot, Dispatcher,  F
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


def add_user(message: Message):
    
    print(message.message_id, message.from_user.id)
    con = connection(config)
    try:
        with con.cursor() as cursor:
            insert_query = f'INSERT INTO user (`iduser`,`type`, `country`, `genre`, `actor`)'\
            f'VALUES({message.from_user.id}, null, null, null, null);'
            cursor.execute(insert_query)
            con.commit()
            print("Аккаунт создан")
    except Exception as ex:
        print(ex)
        print("Ошибка работы бд")
            
            
def have_user(message: Message) -> bool:

    try:
        con = connection(config)
        with con.cursor() as cursor:
            find_user = f"SELECT * FROM user WHERE iduser = {message.from_user.id}"
            cursor.execute(find_user)
            result = cursor.fetchone()
            # if a row is returned, the user exists in the database
            if result is not None:
                print(result)
                return True
            else:
                return False
    except Exception as ex:
        print(ex)
        return False



def state_user(msg: Message) -> str:
    try:
        con = connection(config)
        with con.cursor() as cursor:
            select_user =  f"SELECT type FROM user WHERE iduser = {msg.from_user.id}"
            cursor.execute(select_user)
            result = cursor.fetchone()
            state = result['type']
            return state
    except Exception as ex:
        print(ex)

async def update_user(msg: Message, type: str = None, genre_user: str = None, country: str = None, actor: str = None):
    try:
        con = connection(config)
        if genre_user is not None:
            with con.cursor() as cursor:
                update = f"UPDATE user SET genre = '{genre_user}', country = '{None}', actor = '{None}' WHERE iduser = {msg.from_user.id}"                    
                cursor.execute(update)
                con.commit()
        if country is not None:
            with con.cursor() as cursor:
                update = f"UPDATE user SET genre = '{None}', country = '{country}', actor = '{None}' WHERE iduser = {msg.from_user.id}"                    
                cursor.execute(update)
                con.commit() 
        if actor is not None:
            with con.cursor() as cursor:
                update = f"UPDATE user SET genre = '{None}', country = '{None}', actor = '{actor}' WHERE iduser = {msg.from_user.id}"                    
                cursor.execute(update)
                con.commit()    
        if type is not None:
            with con.cursor() as cursor:
                update = f"UPDATE user SET type = '{type}' WHERE iduser = {msg.from_user.id}"                    
                cursor.execute(update)
                con.commit()  
        
        
    except Exception as ex:
        print(ex)




async def random_movie(msg: Message) -> str:
    
    con = connection(config)
    with con.cursor() as cursor:
        try:           

            cursor.execute(f"SELECT genre FROM user WHERE iduser = {msg.from_user.id}")
            genre_user = cursor.fetchone()

            cursor.execute(f"SELECT country FROM user WHERE iduser = {msg.from_user.id}")
            country_user = cursor.fetchone()
            
            cursor.execute(f"SELECT actor FROM user WHERE iduser = {msg.from_user.id}")
            actor_user = cursor.fetchone()

            genre = genre_user['genre']
            country = country_user['country']
            actor = actor_user['actor']

            print( genre, country, actor)

        except KeyError:
            print("The specified row does not exist.")
            
    with con.cursor() as cursor:
        if genre != 'None':
                query = "SELECT * FROM `movie` WHERE genre = %s ORDER BY RAND() LIMIT 1"
                cursor.execute(query, (genre,))
                result = cursor.fetchone()
                title :str = result['title']
                description :str= result['description'] 
                runtime :str  = result['runtime']
                print(title, description, runtime)
                message_res = f"{title} ({runtime})\n\n{description}"
                #print(message_res)
                return message_res
                
        if country != 'None':
                query = "SELECT * FROM `movie` WHERE country = %s ORDER BY RAND() LIMIT 1"
                cursor.execute(query, (country,))
                result = cursor.fetchone()
                title :str = result['title']
                description :str= result['description'] 
                runtime :str  = result['runtime']
                print(title, description, runtime)
                message_res = f"{title} ({runtime})\n\n{description}"
                #print(message_res)
                return message_res
                
        if actor != 'None':
                query = f"SELECT * FROM `movie` JOIN `movie_cast` ON `idmovie` = `movie_idmovie` JOIN `actor` ON `idactor` = `actor_idactor` WHERE name ='{msg.text}' ORDER BY RAND() LIMIT 1"
                cursor.execute(query)
                result = cursor.fetchone()
                title :str = result['title']
                description :str= result['description'] 
                runtime :str  = result['runtime']
                print(title, description, runtime)
                message_res = f"{title} ({runtime})\n\n{description}"
                #print(message_res)
                return message_res
                    
               
            
            
         
       
            
    
    #print(result)

    #message_res = f"{title} ({runtime})\n\n{description}"
    #print(message_res)
    #return message_res



async def actor_biography(name: str):
    con = connection(config)
    with con.cursor() as cursor:
        try:           
            cursor.execute(f"SELECT biography FROM actor WHERE name = '{name}'")
            result = cursor.fetchone()
            con.commit()  
        except KeyError:
            print("The specified row does not exist.")

    biography :str = result['biography']

    message = f"{name}\n\n{biography}"
    print(message)
    return message


async def actor_facts(name: str):
    con = connection(config)
    with con.cursor() as cursor:
        try:           
            cursor.execute(f"SELECT facts FROM actor WHERE name = '{name}'")
            result = cursor.fetchone()
            con.commit()  
        except KeyError:
            print("The specified row does not exist.")

    fact :str = result['facts']

    message = f"{name}\n\n{fact}"
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