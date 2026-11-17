
from fastapi import FastAPI

from database import Base, engine
from models.user_model import User
from routers.user_router import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TalentConnect API",
    description="Multi-Category Talent and Service Booking Platform",
    version="1.0.0"
)

app.include_router(user_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to TalentConnect API"
    }


