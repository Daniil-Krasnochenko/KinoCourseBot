import asyncio
import logging
import pymysql
from aiogram import types
import database 
from aiogram import Bot, Dispatcher
from config import Config, load_config
from set_menu import set_main_menu
import h_func
async def main() -> None:
    # Загружаем конфиг в переменную config
    config: Config = load_config(r"C:\Users\Kras.nyi\Desktop\KinoCourse\.env")
 
    
    logger = logging.getLogger(__name__)

     # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    # Инициализируем бот и диспетчер
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()
    
    dp.include_router(h_func.router)
    dp.include_router(database.router)
    
    await set_main_menu(bot)

    # Пропускаем накопившиеся апдейты и запускаем polling
    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
