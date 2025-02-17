import asyncio
from aiogram import Bot, Dispatcher
from config import Config
from database.db import db_start
from handlers.booking import router as booking_router

# Инициализация бота и диспетчера
bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()

# Подключение роутеров
dp.include_router(booking_router)


# Функция для инициализации базы данных
async def on_startup():
    await db_start()  # Инициализация базы данных при запуске бота


# Основная функция для запуска бота
async def main():
    await on_startup()  # Выполняем инициализацию базы данных
    await dp.start_polling(bot)


# Запуск бота
if __name__ == '__main__':
    asyncio.run(main())
