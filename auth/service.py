from datetime import datetime, timedelta
from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from database.dependency import get_session
from settings import settings
from user.model import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


def auth_user(session: Session = Depends(get_session), token: str = Depends(oauth2_scheme)) -> User:
    return token_auth_user(session, token)


def auth_admin(token: Annotated[str, Depends(oauth2_scheme)], session: Session = Depends(get_session)) -> User:
    user = token_auth_user(session, token)
    if not user.is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


def cred_auth_user(session: Session, username: str, password: str):
    user = session.query(User).where(User.username == username).first()
    if not isinstance(user, User) or not user.verify_password(password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


def token_auth_user(session: Session, token: str):
    expire, username = decode_access_token(token).values()
    user = session.query(User).where(User.username == username).first()
    if not isinstance(user, User) or datetime.now().timestamp() > expire:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user


def encode_access_token(claims: dict) -> str:
    return jwt.encode(claims, key=settings.ACCESSTOKEN_SECRET_KEY, algorithm=settings.ALGORITHM)


def encode_refresh_token(claims: dict) -> str:
    return jwt.encode(claims, key=settings.REFRESHTOKEN_SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, key=settings.ACCESSTOKEN_SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def decode_refresh_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, key=settings.REFRESHTOKEN_SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def create_access_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = encode_access_token({"exp": expire, "sub": username})

    return token


def create_refresh_token(username: str) -> str:
    expire = datetime.utcnow() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    token = encode_refresh_token({"exp": expire, "sub": username})
    return token


def refresh_access_token(session: Session, refresh_token: str) -> str:
    expire, username = decode_access_token(refresh_token).values()

    if datetime.now().timestamp() > expire:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = token_auth_user(session, refresh_token)
    token = create_access_token(user.username)
    return token
