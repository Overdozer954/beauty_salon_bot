import asyncio
from aiogram import Bot, Dispatcher
from config import Config
from handlers.booking import router as booking_router

bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher(bot)

dp.include_router(booking_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())