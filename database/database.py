import os
from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if os.environ.get('POSTGRES_USER'):
    DATABASE_URL = f"postgresql://{environ['POSTGRES_USER']}:{environ['POSTGRES_PASSWORD']}@db/{environ['POSTGRES_DB']}"
    engine = create_engine(DATABASE_URL)
else:
    DATABASE_URL = "sqlite:///./test_db.db"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
