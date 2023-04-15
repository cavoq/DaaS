from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Attack(Base):
    __tablename__ = 'attacks'
    id = Column(Integer, primary_key=True)
    layer = Column(String, nullable=False)
    type = Column(String, nullable=False)
    ts_start = Column(DateTime, nullable=False)
    ts_end = Column(DateTime, nullable=False)
    status = Column(String, nullable=False)
    api_key_id = Column(Integer, ForeignKey('api_keys.id'))
    api_key = relationship("ApiKey", back_populates="attacks")


class ApiKey(Base):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    ts_created = Column(DateTime, nullable=False)
    ts_expired = Column(DateTime, nullable=False)
    attacks = relationship("Attack", back_populates="api_key")
