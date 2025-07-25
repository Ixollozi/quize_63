from fastapi import FastAPI
from api.users import user_router
from api.questions import question_router
from database.models import create_tables
create_tables()

app = FastAPI()

app.include_router(user_router)
app.include_router(question_router)