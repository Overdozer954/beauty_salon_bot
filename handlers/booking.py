from aiogram import types, Router
from aiogram.filters import Command
from database.db import get_db
from services.google_calendar import create_event
from database.models import bookings

router = Router()

@router.message(Command("book"))
async def start_booking(message: types.Message):
    await message.answer("Пожалуйста, выберите дату для записи.")

@router.callback_query(lambda c: c.data.startswith('date_'))
async def confirm_booking(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    date = callback.data  # Дата из callback
    db = get_db()
    db.execute(
        bookings.insert().values(
            user_id=user_id,
            date=date
        )
    )
    db.commit()
    create_event(date)
    await callback.message.answer("Вы успешно записаны!")