from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


# Приветственное сообщение и меню
@router.message(Command("start"))
async def start_command(message: types.Message):
    # Создаем клавиатуру с кнопками
    builder = ReplyKeyboardBuilder()
    builder.row(
        types.KeyboardButton(text="📅 Записаться на процедуру"),
        types.KeyboardButton(text="💆 Наши услуги"),
    )
    builder.row(
        types.KeyboardButton(text="📞 Контакты"),
        types.KeyboardButton(text="ℹ️ О нас"),
    )

    # Отправляем приветственное сообщение
    await message.answer(
        "Добро пожаловать в OxiBeauty! 🎀\n\n"
        "Мы — ваш лучший выбор для красоты и расслабления в центре Риги. "
        "Выберите действие из меню ниже:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


# Обработка кнопки "О нас"
@router.message(lambda message: message.text == "ℹ️ О нас")
async def about_us(message: types.Message):
    await message.answer(
        "OxiBeauty — место, где элегантность встречается с заботой. 💖\n\n"
        "Мы находимся по адресу Лиенес 6, Рига. "
        "Наши услуги включают профессиональные массажи, эпиляцию и премиальные процедуры для вашей красоты."
    )


# Обработка кнопки "Наши услуги"
@router.message(lambda message: message.text == "💆 Наши услуги")
async def services(message: types.Message):
    await message.answer(
        "Наши услуги:\n\n"
        "💆 **Массаж**: Расслабляющий и антицеллюлитный массаж.\n"
        "✨ **Эпиляция**: Бережное удаление волос для гладкой кожи.\n"
        "💎 **Beautylizer**: Инновационные процедуры для сияющей кожи.\n\n"
        "Выберите услугу для записи."
    )


# Обработка кнопки "Контакты"
@router.message(lambda message: message.text == "📞 Контакты")
async def contacts(message: types.Message):
    await message.answer(
        "Наши контакты:\n\n"
        "📍 Адрес: Лиенес 6, Рига\n"
        "📞 Телефон: +371 25403503\n"
        "🌐 Сайт: https://oxibeauty.lv\n\n"
        "Мы ждем вас!"
    )


# Обработка кнопки "Записаться на процедуру"
@router.message(lambda message: message.text == "📅 Записаться на процедуру")
async def book_service(message: types.Message):
    await message.answer(
        "Чтобы записаться на процедуру, выберите категорию услуги:\n\n"
        "1. Массаж\n"
        "2. Эпиляция\n"
        "3. Beautylizer\n\n"
        "Напишите номер категории, на которую хотите записаться."
    )


# Обработка выбора категории услуги
@router.message(lambda message: message.text in ["1", "2", "3"])
async def choose_service_category(message: types.Message):
    categories = {
        "1": "Массаж",
        "2": "Эпиляция",
        "3": "Beautylizer",
    }
    category = categories[message.text]

    await message.answer(
        f"Вы выбрали категорию: {category}.\n\n"
        "Теперь выберите конкретную услугу из списка ниже:\n\n"
        "1. Услуга 1\n"
        "2. Услуга 2\n"
        "3. Услуга 3\n\n"
        "Напишите номер услуги, на которую хотите записаться."
    )


# Обработка выбора конкретной услуги
@router.message(lambda message: message.text in ["1", "2", "3"])
async def choose_service(message: types.Message):
    services = {
        "1": "Классический массаж (Полное тело) - 40€",
        "2": "Эпиляция подмышек + Бикини - 55€",
        "3": "Beautylizer (1 зона) - 40€",
    }
    service = services[message.text]

    await message.answer(
        f"Вы выбрали услугу: {service}.\n\n"
        "Теперь выберите удобную дату и время для записи.\n\n"
        "Напишите дату в формате ДД.ММ.ГГГГ (например, 25.10.2023)."
    )


# Обработка выбора даты
@router.message(lambda message: message.text.count(".") == 2)
async def choose_date(message: types.Message):
    await message.answer(
        f"Вы выбрали дату: {message.text}.\n\n"
        "Теперь выберите удобное время для записи.\n\n"
        "Напишите время в формате ЧЧ:ММ (например, 14:00)."
    )


# Обработка выбора времени
@router.message(lambda message: message.text.count(":") == 1)
async def choose_time(message: types.Message):
    await message.answer(
        f"Вы выбрали время: {message.text}.\n\n"
        "Спасибо за запись! Мы свяжемся с вами для подтверждения."
    )
