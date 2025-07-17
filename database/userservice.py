from sqlalchemy.orm import Session
from database.models import User, Question,UserAnswer, Rating


# Создание юзера

def create_user_db(db: Session, name: str, phone: str):
    user = db.query(User).filter(User.name == name).first()
    if user:
        return user.id
    new_user = User(name=name, phone=phone)
    db.add(new_user)
    db.commit()
    return  new_user.id

# получение юзера по айди
def get_user_by_id_db(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# Ответ пользователя
def save_user_answer_db(db: Session, user_id: int, question_id: int, user_answer:int):
    question = db.query(Question).filter(Question.id == question_id).first()

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
    if is_correct:
        update_rating_db(db, user_id, question.level)

    return is_correct

# прописать функцию def update_rating_db

def update_rating_db(db: Session, user_id: int, level: str):
    rating = db.query(Rating).filter(
        Rating.user_id == user_id,
        Rating.level == level
    ).first()
    if rating:
        rating.correct_answer +=1
    else:
        new_rating = Rating(
            user_id=user_id,
            correct_answer=1,
            level=level
        )
        db.add(new_rating)
    db.commit()



def update_user_avatar_db(db: Session,user_id: int, file_path: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.avatar = file_path
        db.commit()
        return True
    return False
