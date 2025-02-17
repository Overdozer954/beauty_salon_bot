from aiogram import types
from services.nlp_service import NLPService
from config import Config

nlp_service = NLPService(Config.OPENAI_API_KEY)

async def handle_message(message: types.Message):
    user_message = message.text
    response = await nlp_service.get_response(user_message)
    await message.answer(response)