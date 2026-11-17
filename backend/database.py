from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
from urllib.parse import quote_plus

DB_PASSWORD = quote_plus("Piano@9059242004")

DATABASE_URL = (f"postgresql+psycopg://postgres:{DB_PASSWORD}""@localhost:5432/talentconnect")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()