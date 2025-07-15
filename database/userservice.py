from sqlalchemy.orm import Session
from models import User, Question,UserAnswer, Rating


# Создание юзера

def create_user_db(db: Session, name: str, phone: str):
    user = db.query(User).filter(User.name == name).first()
    if user:
        return user.id
    db.add(user)
    db.commit()
    return  user.id

# получение юзера по айди
def get_user_by_id_db(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Ответ пользователя
def save_user_answer_db(db: Session, user_id: int, question_id: int, user_answer:str):
    question = db.query(Question).filter(Question.id == question_id).fisrt()
    if not question:
        return False

    is_correct = (question.correct_answer == user_answer)

    new_answer = UserAnswer(
        user_id=user_id,
        user_answer=user_answer,
        question_id=question_id,
        correctness=is_correct,
        level=question.level
    )
    db.add(new_answer)
    db.commit()

# прописать функцию def update_rating_db

