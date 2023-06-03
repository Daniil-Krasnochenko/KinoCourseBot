from aiogram import Router, Bot, F
import asyncio
from time import sleep
from aiogram.filters.state import StatesGroup, State 
from aiogram.filters import StateFilter
from typing import Optional
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message, CallbackQuery, ContentType, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from synth import  *
from lexicon import LEXICON_RU, ACTORS
from database import update_user, add_user, have_user, state_user, random_movie, actor_biography, actor_facts
from config import Config, load_config

config: Config = load_config(r"C:\Users\Kras.nyi\Desktop\KinoCourse\.env")
bot: Bot = Bot(token=config.tg_bot.token)
# Этот хэндлер срабатывает на команду /start
router: Router = Router()

last_name: str 

# Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
class FSMFillForm(StatesGroup):
    # Создаем экземпляры класса State, последовательно
    # перечисляя возможные состояния, в которых будет находиться
    # бот в разные моменты взаимодейтсвия с пользователем
    actor_name = State()        # Состояние ожидания ввода имени

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=find_kb)
    test_user = have_user(message)
    print(test_user)
    if test_user == False:
        add_user(message)



# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=cancel_menu)

#ХРЕНЬ
# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands=['menu']))
async def menu_func(message: Message):
    await message.answer(text=LEXICON_RU['cancel_menu'], reply_markup=find_kb)

@router.message(Text(text=LEXICON_RU['menu']))
async def cancel_menu_func(message: Message):
    await message.answer(text=LEXICON_RU['cancel_menu'], reply_markup=find_kb)
    
 #меню актёра
@router.message(Text(text=LEXICON_RU['actor_button']))
async def menu_actor(message: Message):
    await update_user(message, type = "Actor")
    await actor_name(message)
    
    
@router.message(Text(text=LEXICON_RU['biography']))
async def biography_func(message: Message):
    global last_name
    biography = await actor_biography(last_name)
    await message.answer(text=biography, reply_markup=cancel_menu)    
    
@router.message(Text(text=LEXICON_RU['interesting_facts']))
async def facts_func(message: Message):
    global last_name
    fact = await actor_facts(last_name)
    await message.answer(text=fact, reply_markup=cancel_menu)          

# меню фильмов
 
@router.message(Text(text=LEXICON_RU['film_button']))
async def film_func(message: Message):
    await update_user(message, type="Film")
    await message.answer(text=LEXICON_RU['movie_find'], reply_markup=type_kb)

@router.message(Text(text=LEXICON_RU['genre']))
async def genre_func(message: Message):
    await message.answer(text="Выберите предпочитаемый жанр", reply_markup=genre)    
    
    
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
        genre = LEXICON_RU['fantastic']
    if message.text == LEXICON_RU['comedy']:
        genre = LEXICON_RU['comedy']
    if message.text == LEXICON_RU['adventures']:
        genre = LEXICON_RU['adventures']
    if message.text == LEXICON_RU['fantasy']:
        genre = LEXICON_RU['fantasy']
    if message.text == LEXICON_RU['drama']:
        genre = LEXICON_RU['drama']
    if message.text == LEXICON_RU['action_movie']:
        genre = LEXICON_RU['action_movie']
    if message.text == LEXICON_RU['criminal']:
        genre = LEXICON_RU['criminal']
    if message.text == LEXICON_RU['war_movie']:
        genre = LEXICON_RU['war_movie']

    await update_user(message, genre_user=genre)
    await display_random(message)
    




@router.message(Text(text=LEXICON_RU['country']))
async def country_func(message: Message):
    await message.answer(text='Выберите страну', reply_markup=country)    
    
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
        country = LEXICON_RU['russia']
    if message.text == LEXICON_RU['usa']:
        country = LEXICON_RU['usa']
    if message.text == LEXICON_RU['great_britain']:
        country = LEXICON_RU['great_britain']
    if message.text == LEXICON_RU['germany']:
        country = LEXICON_RU['germany']
    if message.text == LEXICON_RU['china']:
        country = LEXICON_RU['china']
    if message.text == LEXICON_RU['norway']:
        country = LEXICON_RU['norway']
    if message.text == LEXICON_RU['new_zealand']:
        country = LEXICON_RU['new_zealand']
    if message.text == LEXICON_RU['australia']:
        country = LEXICON_RU['australia']

    await update_user(message, country=country)
    await display_random(message)  
    
  
@router.message(Text(text=LEXICON_RU['other']))
async def other_button(message: Message):
    await display_random(message)


@router.message(Text(text=LEXICON_RU['end']))
async def end_button(message: Message):
    await update_user(message, type=None)
    await message.answer(text='Хорошо, закончили!', reply_markup=find_kb)
   

@router.message(Text(text=LEXICON_RU['actor']))
async def actor_name(message: Message):
    
    await message.answer(text="Ведите имя и фамилию актера", reply_markup=ReplyKeyboardRemove())
    print("Зашло")
    # Устанавливаем состояние ожидания ввода имени
   # await state.set_state(FSMFillForm.actor_name)
    

@router.message()
async def actor_func(message: Message):
    global last_name
    last_name = message.text
    if last_name in ACTORS:
        state = state_user(message)
        print(last_name)
        if state == "Film" :
            await update_user(message, actor=last_name)
            await display_random(message)
        if state == "Actor":
            print("ура")
            await message.answer(text=LEXICON_RU['actor_question'], reply_markup=actor_kb)
        else:
            print("неееееееееееет")
    else:
        await message.answer(text="Сорьки, я не понял")






async def display_random(message: Message):
    message_user = await random_movie(message)
    await message.answer(text=message_user, reply_markup=poisk_kb)
    

