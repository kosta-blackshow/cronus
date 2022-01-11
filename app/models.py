from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import (
    DateTime,
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))
    posts = relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    body = Column(String(140))
    timestamp = Column(DateTime, index=True, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
