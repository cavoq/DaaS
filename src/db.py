"""Database connection and session management."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.engine = create_engine(*args, **kwargs)
            Base.metadata.create_all(cls._instance.engine)
            cls._instance.sessionmaker = sessionmaker(
                bind=cls._instance.engine)
        return cls._instance

    @staticmethod
    def get_session():
        return Database()._instance.sessionmaker()

    @staticmethod
    def close():
        Database()._instance.engine.dispose()
