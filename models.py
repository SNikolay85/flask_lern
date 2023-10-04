import atexit
import os
from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

POSTGRES_DB = os.getenv('POSTGRES_DB', 'my_db')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'my_user')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'my_password')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', 5431)

#DSN = f'postgresql://postgres:{pas}@localhost:5432/magazine_of_publisher'
#engine = sq.create_engine(DSN)
DSN = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
engine = create_engine(DSN)
atexit.register(engine.dispose)

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class User(Base):

    __tablename__ = 'app_users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())


Base.metadata.create_all()
