from aiogram import Router, Bot
import asyncio
from aiogram.filters.state import StatesGroup, State
from typing import Optional
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove
from synth import  *
from lexicon import LEXICON_RU
from database import update_user, genre_random_atributs, country_random_atributs
from config import Config, load_config

config: Config = load_config(r"C:\Users\Kras.nyi\Desktop\KinoCourse\.env")
bot: Bot = Bot(token=config.tg_bot.token)
# Этот хэндлер срабатывает на команду /start
router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=find_kb)



# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=cancel_menu)

# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['menu']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/menu'], reply_markup=find_kb)
    
    
 #меню актёра
@router.message(Text(text=LEXICON_RU['actor_button']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['actor_question'], reply_markup=actor_kb)
    
@router.message(Text(text=LEXICON_RU['biography']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['actor_question'], reply_markup=biography_button)    
    
@router.message(Text(text=LEXICON_RU['interesting_facts']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['actor_question'], reply_markup=interesting_facts_button)        

# меню фильмов
 
@router.message(Text(text=LEXICON_RU['film_button']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['movie_find'], reply_markup=type_kb)

@router.message(Text(text=LEXICON_RU['genre']))
async def process_help_command(message: Message):
    await message.answer(text="Выберите предпочитаемый жанр", reply_markup=button_genre)    
    
    
@router.message(Text(text=[LEXICON_RU['fantastic'],
                           LEXICON_RU['comedy'],
                           LEXICON_RU['adventures'],
                           LEXICON_RU['fantasy'],
                           LEXICON_RU['drama'],
                           LEXICON_RU['action_movie'],
                           LEXICON_RU['criminal'],
                           LEXICON_RU['war_movie']]))
async def choice_genre_button(message: Message):
    genre: str
    if message.text == LEXICON_RU['fantastic']:
        genre = 'fantastic'
    if message.text == LEXICON_RU['comedy']:
        genre = 'comedy'
    if message.text == LEXICON_RU['adventures']:
        genre = 'adventures'
    if message.text == LEXICON_RU['fantasy']:
        genre = 'fantasy'
    if message.text == LEXICON_RU['drama']:
        genre = 'drama'
    if message.text == LEXICON_RU['action_movie']:
        genre = 'action_movie'
    if message.text == LEXICON_RU['criminal']:
        genre = 'criminal'
    if message.text == LEXICON_RU['war_movie']:
        genre = 'war_movie'

    await update_user(message, genre=genre)
    

@router.message(Text(text=LEXICON_RU['country']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['movie_find'], reply_markup=button_country)    
    
@router.message(Text(text=[LEXICON_RU['russia'],
                           LEXICON_RU['usa'],
                           LEXICON_RU['great_britain'],
                           LEXICON_RU['germany'],
                           LEXICON_RU['china'],
                           LEXICON_RU['norway'],
                           LEXICON_RU['new_zealand'],
                           LEXICON_RU['australia']]))
async def choice_country_button(message: Message):
    country: str
    if message.text == LEXICON_RU['russia']:
        country = 'russia'
    if message.text == LEXICON_RU['usa']:
        country = 'usa'
    if message.text == LEXICON_RU['great_britain']:
        country = 'great_britain'
    if message.text == LEXICON_RU['germany']:
        country = 'germany'
    if message.text == LEXICON_RU['china']:
        country = 'china'
    if message.text == LEXICON_RU['norway']:
        country = 'norway'
    if message.text == LEXICON_RU['new_zealand']:
        country = 'new_zealand'
    if message.text == LEXICON_RU['australia']:
        country = 'australia'

    await update_user(message, country=country)  


@router.message(Text(text=LEXICON_RU['actor']))
async def process_help_command(message: Message):
    msg = message.text
    await update_user(message, actor= msg)
    await message.answer(text=LEXICON_RU['movie_find'], reply_markup=button_actor)       
    

# Этот хэндлер срабатывает на команду /start
 
@router.message(Text(text=[LEXICON_RU['fantastic'],
                           LEXICON_RU['comedy'],
                           LEXICON_RU['action_movie'],
                           LEXICON_RU['adventures'],
                           LEXICON_RU['criminal'],
                           LEXICON_RU['war_movie'],
                           LEXICON_RU['fantasy'],
                           LEXICON_RU['drama']]))
async def genre_button(message: Message):
    genre: str
    if message.text == LEXICON_RU['fantastic']:
        genre = 'fantastic'
    if message.text == LEXICON_RU['comedy']:
        genre = 'comedy'
    if message.text == LEXICON_RU['action_movie']:
        genre = 'action_movie'
    if message.text == LEXICON_RU['adventures']:
        genre = 'adventures'
    if message.text == LEXICON_RU['criminal']:
        genre = 'criminal'
    if message.text == LEXICON_RU['war_movie']:
        genre = 'war_movie'
    if message.text == LEXICON_RU['fantasy']:
        genre = 'fantasy'
    if message.text == LEXICON_RU['drama']:
        genre = 'drama'
        
    await update_user(message, genre=genre)
    await update_user(message, in_find=True)
    await genre_display_random(message)
async def genre_display_random(message: Message):
    message_user = await genre_random_atributs(message)
    try:
   
        await message.answer_photo(caption=message_user, reply_markup=find_kb)
        print('Image sent successfully')
    except Exception as e:
        print('Error sending image:', e)
@router.message(Text(text=[LEXICON_RU['russia'],
                           LEXICON_RU['usa'],
                           LEXICON_RU['great_britain'],
                           LEXICON_RU['germany'],
                           LEXICON_RU['china'],
                           LEXICON_RU['norway'],
                           LEXICON_RU['new_zealand'],
                           LEXICON_RU['australia'],
                           LEXICON_RU['mexico']]))
async def country_button(message: Message):
    country: str
    if message.text == LEXICON_RU['russia']:
        country = 'russia'
    if message.text == LEXICON_RU['usa']:
        country = 'usa'
    if message.text == LEXICON_RU['great_britain']:
        country = 'great_britain'
    if message.text == LEXICON_RU['germany']:
        country = 'germany'
    if message.text == LEXICON_RU['china']:
        country = 'china'
    if message.text == LEXICON_RU['norway']:
        country = 'norway'
    if message.text == LEXICON_RU['new_zealand']:
        country = 'new_zealand'
    if message.text == LEXICON_RU['australia']:
        country = 'australia'
    if message.text == LEXICON_RU['mexico']:
        country = 'mexico'
        
    await update_user(message, country=country)
    await update_user(message, in_find=True)
    await country_display_random(message)
async def country_display_random(message: Message):
    message_user = await country_random_atributs(message)
    try:
   
        await message.answer_photo(caption=message_user, reply_markup=find_kb)
        print('Image sent successfully')
    except Exception as e:
        print('Error sending image:', e)