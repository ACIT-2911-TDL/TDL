from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import engine
from sqlalchemy.orm import sessionmaker

engine.connect()

Base = declarative_base()
session = sessionmaker(engine)()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    deadline = Column(DateTime, nullable=False)
    complete = Column(Boolean, default=False)
    color = Column(String(10), default=None)


# Drop table in db
# Task.__table__.drop(engine)
# create table in db
# Task.metadata.create_all(engine)


