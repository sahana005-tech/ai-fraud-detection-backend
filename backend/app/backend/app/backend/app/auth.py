from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .db import SessionLocal
from . import models

# ----------------------------
# CONFIGURATION
# ----------------------------
SECRET_KEY = "supersecretkey123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing utility
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ----------------------------
# PASSWORD FUNCTIONS
# ----------------------------
def get_password_hash(password: str) -> str:
    """Hash a plain password."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain password against its hash."""
    return pwd_context.verify(plain_password, hashed_password)

# ----------------------------
# DATABASE SESSION DEPENDENCY
# ----------------------------
def get_db():
    """Create a database session for use in routes."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------
# JWT TOKEN CREATION
# ----------------------------
def create_access_token(data: dict, expires_delta: timedelta = None):
    """Generate a JWT access token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
