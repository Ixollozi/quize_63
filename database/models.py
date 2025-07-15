from email.policy import default

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base, engine


#  Модель юзеров
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)

    name = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)

    reg_date = Column(DateTime, default=datetime.now())

# Модель вопросов
class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, autoincrement=True, primary_key=True)

    main_question = Column(String, nullable=False)
    v1 = Column(String, nullable=False)
    v2 = Column(String, nullable=False)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(Integer, nullable=False)

    level = Column(String, default='Beginner')

class UserAnswer(Base):
    __tablename__ = 'user_answers'
    id = Column(Integer, autoincrement=True, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user_answer = Column(String, nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'))
    correctness = Column(Boolean, nullable=False, default=False)
    level = Column(String)

    # Связь таблиц
    user_fk = relationship(User, lazy='subquery')
    question_fk = relationship(Question, lazy='subquery')

class Rating(Base):
    __tablename__ = 'rating'
    id = Column(Integer, autoincrement=True, primary_key=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    correct_anwer = Column(String, default=0)

    user_fk = relationship(User, lazy='subquery')


def create_tables():
    Base.metadata.create_all(engine)