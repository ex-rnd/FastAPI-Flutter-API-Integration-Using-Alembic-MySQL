from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv


# Database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL",
                         "mysql+pymysql://fastapi:1234@localhost:3306/fruit_db")
engine = create_engine(DATABASE_URL, pool_pre_ping=True)


# DATABASE_URL = os.getenv("DATABASE_URL")

# engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()