from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

# Создаем подключение к базе данных
engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()