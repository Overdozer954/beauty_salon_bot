from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.models import Booking
from database.db import get_db

router = Router()

# Список услуг с временем и ценой
SERVICES = {
    "Массаж": {
        "Классический массаж (Полное тело)": {"1ч": "40€", "1.5ч": "50€", "2ч": "60€"},
        "Горячие камни (Полное тело)": {"1.5ч": "60€", "2ч": "70€"},
        "Антицеллюлитный массаж (2 зоны)": {"45м": "40€", "1ч": "50€"},
        "Антицеллюлитный массаж (Полное тело)": {"1.5ч": "65€"},
        "Релаксирующий массаж (Полное тело)": {"1ч": "40€", "1.5ч": "50€", "2ч": "60€"},
        "Фитнес для лица": {"30м": "30€", "45м": "40€"},
        "Ароматерапевтический массаж (Полное тело)": {"1ч": "40€", "1.5ч": "50€", "2ч": "60€"},
    },
    "Эпиляция": {
        "Подмышки + Бикини": {"-": "55€"},
        "Полное тело": {"-": "99€"},
    },
    "Beautylizer": {
        "Скульптурирование тела (Обёртывание + Массаж)": {"60м": "45€"},
        "BeautyLizer (1 зона)": {"30м": "40€"},
        "BeautyLizer (2 зоны)": {"45м": "55€"},
        "BeautyLizer (Полное тело)": {"1ч": "70€"},
    },
}


# Обработка команды /book или кнопки "Записаться на процедуру"
@router.message(lambda message: message.text == "📅 Записаться на процедуру")
async def book_service(message: types.Message):
    builder = InlineKeyboardBuilder()
    for service in SERVICES:
        builder.button(text=service, callback_data=f"service_{service}")
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await message.answer(
        "Выберите категорию услуги:",
        reply_markup=builder.as_markup(),
    )


# Обработка выбора категории услуги
@router.callback_query(lambda c: c.data.startswith("service_"))
async def choose_service(callback: types.CallbackQuery):
    service_category = callback.data.split("_")[1]
    services = SERVICES[service_category]

    builder = InlineKeyboardBuilder()
    for service_name, details in services.items():
        for duration, price in details.items():
            builder.button(
                text=f"{service_name} ({duration}) - {price}",
                callback_data=f"book_{service_category}_{service_name}_{duration}",
            )
    builder.button(text="⬅️ Назад", callback_data="back_to_categories")
    builder.adjust(1)  # Располагаем кнопки в один столбец

    await callback.message.edit_text(
        f"Выберите услугу из категории '{service_category}':",
        reply_markup=builder.as_markup(),
    )


# Обработка выбора конкретной услуги
@router.callback_query(lambda c: c.data.startswith("book_"))
async def confirm_booking(callback: types.CallbackQuery):
    data = callback.data.split("_")
    service_category = data[1]
    service_name = data[2]
    duration = data[3]
    price = SERVICES[service_category][service_name][duration]

    # Сохраняем запись в базу данных
    db = next(get_db())
    booking = Booking(
        telegram_id=callback.from_user.id,
        telegram_name=callback.from_user.username,
        first_name=callback.from_user.first_name,
        appointed_date="Дата будет выбрана позже",
        appointed_time="Время будет выбрано позже",
        procedure_zone=service_category,
        procedure_type=service_name,
        price=price,
        email="user@example.com",  # Замените на реальный email
        phone="+1234567890",  # Замените на реальный телефон
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    db.close()

    await callback.message.answer(
        f"Вы успешно записались на услугу:\n\n"
        f"**Услуга:** {service_name}\n"
        f"**Категория:** {service_category}\n"
        f"**Длительность:** {duration}\n"
        f"**Цена:** {price}\n\n"
        "Спасибо за выбор OxiBeauty! Мы свяжемся с вами для уточнения даты и времени."
    )


# Обработка кнопки "Назад"
@router.callback_query(lambda c: c.data == "back_to_categories")
async def back_to_categories(callback: types.CallbackQuery):
    builder = InlineKeyboardBuilder()
    for service in SERVICES:
        builder.button(text=service, callback_data=f"service_{service}")
    builder.adjust(1)  # Располагаем кнопки в один столбец
    await callback.message.edit_text(
        "Выберите категорию услуги:",
        reply_markup=builder.as_markup(),
    )
