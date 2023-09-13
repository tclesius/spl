from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth.model import RegisterPost
from auth.service import create_access_token, cred_auth_user, create_refresh_token, \
    decode_refresh_token
from database.dependency import get_session
from invite.model import Invite
from user.model import User

router = APIRouter(prefix="/auth")


@router.post("/token", tags=["auth"])
def get_token(form_data: OAuth2PasswordRequestForm = Depends(),
              session: Session = Depends(get_session)):
    user = cred_auth_user(session, form_data.username, form_data.password)
    return {"access_token": create_access_token(user.username), "refresh_token": create_refresh_token(user.username),
            "token_type": "bearer"}


@router.post("/register", tags=["auth"])
def register(form: RegisterPost, session: Session = Depends(get_session)):
    invite = session.query(Invite).filter(Invite.token == form.invite_token).first()
    if not isinstance(invite, Invite) or invite.accepted:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    user = session.query(User).filter(User.username == form.username).first()
    if user:
        raise HTTPException(status_code=400, detail="Username is already taken")

    # TODO find a way to handle upload for profile picture
    user = User(is_admin=invite.is_admin, username=form.username, password=form.password, email=invite.email)
    session.add(user)
    invite.accepted = True
    session.commit()
    return {"access_token": create_access_token(user.username), "refresh_token": create_refresh_token(user.username),
            "token_type": "bearer"}


@router.post("/refresh", tags=["auth"])
def refresh_access_token(refresh_token: str):
    payload = decode_refresh_token(refresh_token)
    expire, username = payload.values()
    if expire < datetime.now().timestamp():
        raise HTTPException(status_code=401)
    return {"access_token": create_access_token(username), "token_type": "bearer"}
