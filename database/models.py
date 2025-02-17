from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData

metadata = MetaData()

procedures = Table(
    'procedures', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('description', String),
    Column('duration', Integer),
    Column('price', Integer)
)

bookings = Table(
    'bookings', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('procedure_id', Integer),
    Column('date', DateTime)
)