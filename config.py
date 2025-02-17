import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    DATABASE_URL = os.getenv('DATABASE_URL')
    GOOGLE_CALENDAR_ID = os.getenv('GOOGLE_CALENDAR_ID')
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = os.getenv('SMTP_PORT')
    EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Для интеграции с DeepSeek


print(f"BOT_TOKEN: {Config.BOT_TOKEN}")
print(f"DATABASE_URL: {Config.DATABASE_URL}")
