from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class PostIt(Base):
    __tablename__ = 'postit'
    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    date = Column(DateTime, default=datetime.now())

    def __init__(self, title=None, date=None):
        self.title = title
        self.date = date

    def __repr__(self):
        return f'<Title {self.title}>'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    pw = Column(String(128))

    def __init__(self, name=None, pw=None):
        self.name = name,
        self.pw = pw

    def __repr__(self):
        return f'<Name {self.name}>'
