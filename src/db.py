from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    api_key_id = Column(Integer, ForeignKey('api_keys.id'))
    api_key = relationship("ApiKey", back_populates="jobs")

# Define the ApiKey model


class ApiKey(Base):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True)
    jobs = relationship("Job", back_populates="api_key")


# Create a SQLite database engine
engine = create_engine('sqlite:///jobs.db')

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
