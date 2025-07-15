from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# путь субд с которым будем работать
SQLACHEMY_DATABASE_URI = 'sqlite:///data.db'
#создаем движок
engine = create_engine(SQLACHEMY_DATABASE_URI)
# создаем сессии
SessionLocal = sessionmaker(bind=engine)
# для классов
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()