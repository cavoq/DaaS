from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database:
    _instance = None
    _engine = None
    _sessionmaker = None
    _base = declarative_base()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._engine = create_engine(*args, **kwargs)
            cls._base.metadata.create_all(cls._engine)
            cls._sessionmaker = sessionmaker(bind=cls._engine)
        return cls._instance

    @staticmethod
    def get_session():
        return Database()._sessionmaker()

    @staticmethod
    def close():
        Database()._engine.dispose()