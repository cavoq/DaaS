import json
import uuid
from typing import Optional
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from src.db import Database
from datetime import datetime, timedelta
from src.schemas import *

base = Database.get_base()


class Attack(base):
    __tablename__ = 'attacks'

    attack_id = Column(String, nullable=False, primary_key=True, unique=True)
    layer = Column(String, nullable=False)
    type = Column(String, nullable=False)
    ts_start = Column(DateTime, nullable=False)
    ts_end = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    parameters = Column(String, nullable=False)
    elapsed_time = Column(Integer, nullable=True)
    api_key = Column(String, ForeignKey('api_keys.key'))

    def __init__(self, layer: str, attack_type: str, time: int, api_key: str, parameters: dict):
        self.layer = layer
        self.type = attack_type
        self.attack_id = str(uuid.uuid4())
        self.ts_start = datetime.now()
        time_delta = timedelta(seconds=time)
        self.ts_end = self.ts_start + time_delta
        self.status = "Pending"
        self.elapsed_time = 0
        self.parameters = json.dumps(parameters)
        with Database.get_session() as session:
            self.api_key = self.get_api_key(session, api_key)
            self.save(session)

    @staticmethod
    def get_api_key(session: Session, api_key: str) -> Optional['ApiKey']:
        api_key = session.query(ApiKey).filter(
            ApiKey.key == api_key).first().key
        return api_key

    def get_status(self) -> json:
        return json.dumps({
            'attack_id': self.attack_id,
            'layer': self.layer,
            'type': self.type,
            'ts_start': self.ts_start.isoformat(),
            'ts_end': self.ts_end.isoformat(),
            'status': self.status,
            'elapsed_time': self.elapsed_time,
            'parameters': json.loads(self.parameters),
        })

    def update_elapsed_time(self):
        self.elapsed_time = int(
            (datetime.now() - self.ts_start).total_seconds())

    def update(self, key, value):
        with Database.get_session() as session:
            session.query(Attack).filter_by(
                attack_id=self.attack_id).update({key: value})
            session.commit()

    def save(self, session: Session):
        session.add(self)
        session.commit()


class ApiKey(base):
    __tablename__ = 'api_keys'

    key = Column(String, unique=True, primary_key=True)
    ts_created = Column(DateTime, default=datetime.now(), nullable=False)
    ts_expired = Column(DateTime, default=datetime.now() +
                        timedelta(days=30), nullable=False)
    attacks = relationship("Attack")

    def __init__(self, ts_expired: datetime = None):
        self.key = str(uuid.uuid4())
        self.ts_expired = ts_expired

    @staticmethod
    def get_by_key(key: str) -> Optional['ApiKey']:
        with Database.get_session() as session:
            api_key = session.query(ApiKey).filter(ApiKey.key == key).first()
        return api_key
