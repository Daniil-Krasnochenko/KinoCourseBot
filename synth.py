from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
import database
from aiogram.filters import CommandStart
from lexicon import LEXICON_RU





button_menu: KeyboardButton = KeyboardButton(text=LEXICON_RU['menu']) #В меню

# Инициализируем билдер для клавиатуры меню
cancel_menu_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
cancel_menu_builder.row(button_menu, width=2)


# Создаем клавиатуру
cancel_menu = cancel_menu_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)

'''
        button_yes: KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
        button_no: KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])

        # Инициализируем билдер для клавиатуры с кнопками "Да!" и "Не"
        yes_no_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

        # Добавляем кнопки в билдер с параметром width=2
        yes_no_kb_builder.row(button_yes, button_no, width=2)

        # Создаем клавиатуру с кнопками "Да!" и "Не"
        yes_no_kb = yes_no_kb_builder.as_markup(
                                        one_time_keyboard=True,
                                        resize_keyboard=True)
'''



# ------- Клавиатура выбора функции-------

button_actor: KeyboardButton = KeyboardButton(text=LEXICON_RU['actor_button'])
button_film: KeyboardButton = KeyboardButton(text=LEXICON_RU['film_button'])

# Инициализируем билдер для клавиатуры с кнопками "Поиск фильма" и "Поиск актера"
find_kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер с параметром width=2
find_kb_builder.row(button_actor, button_film, width=2)


find_kb = find_kb_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)



button_genre: KeyboardButton = KeyboardButton(text=LEXICON_RU['genre'])
button_country: KeyboardButton = KeyboardButton(text=LEXICON_RU['country'])
button_actor: KeyboardButton = KeyboardButton(text=LEXICON_RU['actor'])

# Создаем клавиатуру типов
type_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[button_genre],
                                              [button_country],
                                              [button_actor]],
                                    one_time_keyboard=True,
                                    resize_keyboard=True)




biography_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['biography'])
interesting_facts_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['interesting_facts'])

# Создаем клавиатуру типов
actor_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                                    keyboard=[[biography_button],
                                              [interesting_facts_button]],
                                    one_time_keyboard=True,
                                    resize_keyboard=True)

# Создаем кнопки с ответами согласия и отказа



# ------- Создаем игровую клавиатуру без использования билдера -------

# Кнопки жанра
fantastic_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['fantastic'])
comedy_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['comedy'])
adventures_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['adventures'])
fantasy_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['fantasy'])
drama_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['drama'])
action_movie_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['action_movie'])
criminal_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['criminal'])
war_movie_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['war_movie'])
'''
genres_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        genres_builder=[[action_movie_button, war_movie_button],
                                [drama_button, comedy_button],
                                [criminal_button, adventures_button],
                                [fantastic_button, fantasy_button]],
                        one_time_keyboard=True,resize_keyboard=True)
'''
genre_builder = ReplyKeyboardBuilder()
genre_builder.row(action_movie_button, war_movie_button, width=2)
genre_builder.row(drama_button, comedy_button, width=2)
genre_builder.row(criminal_button, adventures_button, width=2)
genre_builder.row(fantastic_button, fantasy_button, width=2)
# Создаем клавиатуру "
genre = genre_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)

russia_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['russia'])
usa_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['usa'])
great_britain_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['great_britain'])
germany_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['germany'])
china_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['china'])
norway_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['norway'])
new_zealand_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['new_zealand'])
australia_button: KeyboardButton = KeyboardButton(text=LEXICON_RU['australia'])
'''
genres_builder: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
                        genres_builder=[[action_movie_button, war_movie_button],
                                [drama_button, comedy_button],
                                [criminal_button, adventures_button],
                                [fantastic_button, fantasy_button]],
                        one_time_keyboard=True,resize_keyboard=True)
'''
country_builder = ReplyKeyboardBuilder()
country_builder.row(russia_button, usa_button, width=2)
country_builder.row(great_britain_button, germany_button, width=2)
country_builder.row(china_button, norway_button, width=2)
country_builder.row(new_zealand_button, australia_button, width=2)

# Создаем клавиатуру "
country = country_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)

# ------- Клавиатура во время поиска -------

# Создаем кнопки Другое и Закончить поиск
button_other: KeyboardButton = KeyboardButton(text=LEXICON_RU['other'])
button_end: KeyboardButton = KeyboardButton(text=LEXICON_RU['end'])

poisk_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

poisk_builder.row(button_other, button_end , width=2)

poisk_kb = poisk_builder.as_markup(
                                one_time_keyboard=True,
                                resize_keyboard=True)

