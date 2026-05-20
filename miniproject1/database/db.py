#  database/db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://gumang13:123456@localhost:3306/gumang13"

# 데이터베이스 연결 - echo는 실행하는 sql 출력(개발시 또는 로그기록용)
engine = create_engine(DB_URL, echo=True)

# DB 쿼리문 실행 시킬 객체
SessionLocal = sessionmaker( autocommit=False, autoflush=False,
                            bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()