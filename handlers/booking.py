from aiogram import types, Router
from aiogram.filters import Command
from database.db import get_db
from services.google_calendar import create_event
from database.models import Booking

router = Router()


@router.message(Command("book"))
async def start_booking(message: types.Message):
    await message.answer("Пожалуйста, выберите дату для записи.")


@router.callback_query(lambda c: c.data.startswith('date_'))
async def confirm_booking(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    date = callback.data  # Дата из callback
    db = next(get_db())  # Получаем сессию базы данных
    booking = Booking(
        telegram_id=user_id,
        telegram_name=callback.from_user.username,
        first_name=callback.from_user.first_name,
        appointed_date=date,
        appointed_time="12:00",  # Пример времени
        procedure_zone="Лицо",  # Пример зоны
        procedure_type="Массаж",  # Пример процедуры
        price="1000 руб",  # Пример цены
        email="user@example.com",  # Пример email
        phone="+1234567890"  # Пример телефона
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    db.close()
    await callback.message.answer("Вы успешно записаны!")
