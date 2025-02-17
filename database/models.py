from sqlalchemy import Column, Integer, BigInteger, String, Text, DateTime
from database.db import Base  # Импортируем Base из db.py


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger, nullable=False)
    telegram_name = Column(String)
    first_name = Column(String)


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger, nullable=False)
    telegram_name = Column(String)
    first_name = Column(String)
    appointed_date = Column(String)
    appointed_time = Column(String)
    procedure_zone = Column(String)
    procedure_type = Column(String)
    price = Column(String)
    email = Column(String)
    phone = Column(String)


class Procedure(Base):
    __tablename__ = 'procedures'

    id = Column(Integer, primary_key=True, autoincrement=True)
    procedure_zone = Column(String)
    procedure_type = Column(String)
    price = Column(String)
