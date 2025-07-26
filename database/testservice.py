from sqlalchemy.orm import Session
from database.models import Question, Rating

def add_question_db(db: Session, question_data: dict):
    new_qeustion = Question(
        main_question=question_data['main_question'],
        v1 = question_data['v1'], # Error
        v2 = question_data['v2'],
        v3 = question_data.get('v3'), # None
        v4 = question_data.get('v4'),
        correct_answer = question_data['correct_answer'],
        level = question_data['level']
    )
    db.add(new_qeustion)
    db.commit()

def show_questions_by_level_db(db: Session, level:str):
    return db.query(Question).filter(Question.level == level).all()

def get_top_user_db(db: Session, level: str, limit: int = 5):
    top = (db.query(Rating)
           .filter(Rating.level == level)
           .order_by(Rating.correct_answer.desc())
           .limit(limit)
           ).all()
    return top