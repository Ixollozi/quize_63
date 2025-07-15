from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):

    name: str
    phone: str
    reg_time: datetime

class Question(BaseModel):
    main_question: str
    v1: str
    v2: str
    v3: Optional[str] = None
    v4: Optional[str] = None
    correct_answer: int

    level: Optional[str] = 'Beginner'

class UserAnswer(BaseModel):

    user_id: int
    user_answer: str
    question_id: int

    level: Optional[str] = 'Beginner'


