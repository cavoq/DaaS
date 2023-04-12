from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    layer = Column(String, required=True)
    type = Column(String, required=True)
    ts_start = Column(DateTime, required=True)
    ts_end = Column(DateTime, required=True)
    status = Column(String, required=True)
    api_key_id = Column(Integer, ForeignKey('api_keys.id'))
    api_key = relationship("ApiKey", back_populates="jobs")


class ApiKey(Base):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    jobs = relationship("Job", back_populates="api_key")
