from typing import Optional
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.db import Database
from datetime import datetime
from sqlalchemy.sql import text


class Attack(Database.Base):
    __tablename__ = 'attacks'
    id = Column(Integer, primary_key=True)
    layer = Column(String, nullable=False)
    type = Column(String, nullable=False)
    ts_start = Column(DateTime, nullable=False)
    ts_end = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    api_key_id = Column(Integer, ForeignKey('api_keys.id'))
    api_key = relationship("ApiKey", back_populates="attacks")

    def __init__(self, layer: str, attack_type: str, api_key: str):
        self.layer = layer
        self.type = attack_type
        self.ts_start = datetime.now()
        self.ts_end = datetime.now()
        self.status = "Pending"
        self.api_key_id = self.get_api_key_id(api_key)

    @staticmethod
    def get_api_key_id(api_key: str) -> Optional[int]:
        with Database.get_session() as session:
            result = session.execute(text('SELECT id FROM api_keys WHERE key=:api_key'), {'api_key': api_key})
            api_key_id = result.scalar()
        return api_key_id

    def set_status(self, status: str):
        self.status = status

    


class ApiKey(Database.Base):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    ts_created = Column(DateTime, nullable=False)
    ts_expired = Column(DateTime, nullable=False)
    attacks = relationship("Attack", back_populates="api_key")

    def __init__(self, key: str, ts_created: datetime, ts_expired: datetime):
        self.key = key
        self.ts_created = ts_created
        self.ts_expired = ts_expired

    @staticmethod
    def get_by_key(key: str) -> Optional['ApiKey']:
        with Database.get_session() as session:
            api_key = session.query(ApiKey).filter(ApiKey.key == key).first()
        return api_key