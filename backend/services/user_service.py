
from sqlalchemy.orm import Session
from pwdlib import PasswordHash

from models.user_model import User
from schemas.user_schema import UserCreate


password_hash = PasswordHash.recommended()


def get_password_hash(password: str):
    return password_hash.hash(password)


def register_user(db: Session, user_data: UserCreate):

    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        return None

    hashed_password = get_password_hash(user_data.password)

    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        hashed_password=hashed_password,
        phone_number=user_data.phone_number,
        role=user_data.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)


def authenticate_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if user is None:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
