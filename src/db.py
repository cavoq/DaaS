from sqlalchemy import Engine, create_engine
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
            cls._sessionmaker = sessionmaker(bind=cls._engine, expire_on_commit=False)
        return cls._instance

    @staticmethod
    def get_base() -> declarative_base:
        return Database._base

    @staticmethod
    def get_session() -> sessionmaker:
        return Database._sessionmaker()

    @staticmethod
    def get_engine() -> Engine:
        return Database._engine

    @staticmethod
    def close():
        Database._engine.dispose()
