from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database: str         # Название базы данных
    db_host: str          # URL-адрес базы данных
    db_user: str          # Username пользователя базы данных
    db_password: str
    db_port: str
    

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
def load_config(path: str | None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')),
                db=DatabaseConfig(database=env('DATABASE'),
                                  db_host=env('DB_HOST'),
                                  db_user=env('DB_USER'),
                                  db_password=env('DB_PASSWORD'),
                                  db_port=env('DB_PORT')))


# Выводим значения полей экземпляра класса Config на печать, 
# чтобы убедиться, что все данные, получаемые из переменных окружения, доступны
'''
$Env:BOT_TOKEN="6129398682:AAFn4V3ZxVWfLQH2VnFgKQ972i3Sj-3NhC4"
$Env:DATABASE="KinoCourse"
$Env:DB_HOST="127.0.0.1"
$Env:DB_USER="Daniil_Krasnochenko"
$Env:DB_PASSWORD="9081901303"
$Env:DB_PORT="3306"
'''