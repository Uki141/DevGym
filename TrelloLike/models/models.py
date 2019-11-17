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
