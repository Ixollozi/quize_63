from fastapi import Depends, APIRouter, HTTPException
from schemas import User, Question, UserAnswer
from sqlalchemy.orm import Session
from database import get_db
from database.testservice import add_question_db, show_questions_by_level_db, get_top_user_db


question_router = APIRouter(prefix='/questions', tags=['Вопросы'])


@question_router.post('/new_question')
def new_question(question: Question, db: Session = Depends(get_db)):
    try:
        questions_data = question.dict()
        new_question = add_question_db(db, questions_data)
        return {'message': 'Вопрос добавлен',
                "new_question": new_question}
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Ошибка при добавлении вопроса {e}')


@question_router.get('/level/{level}')
def get_question_by_level(level: str, db: Session = Depends(get_db)):
    get_questions = show_questions_by_level_db(db, level)

    result = []
    for i in get_questions:
        result.append({
            'id': i.id,
            'main_question': i.main_question,
            'v1': i.v1,
            'v2': i.v2,
            'v3': i.v3,
            'v14': i.v4,
            'level': level
        })
    return {'questions': result}


@question_router.get('/top/{level}')
def get_top_users(level: str, db:Session = Depends(get_db)):
    top_users = get_top_user_db(db, level, 10)

    result = []
    for i in top_users:
        result.append({
            'user_name': i.user_fk.name,
            'correct_answer': i.correct_answer,
            'level': i.level
        })
    return {'top_users': top_users}
