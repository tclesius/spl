from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.service import auth_admin, auth_user
from database.dependency import get_session
from invite.model import Invite
from user.model import User

router = APIRouter(prefix="/user", tags=["user"])


@router.patch("/change-password", tags=["admin"], summary="Change the password of a user")
def change_user_password(user_id: int, new_password: str, admin: User = Depends(auth_admin),
                         session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not isinstance(user, User):
        raise HTTPException(status_code=404, detail="User not found")
    user.set_password(new_password)
    session.commit()
    return {"message": "Password changed successfully"}


@router.delete("/remove", tags=["admin"], summary="Remove a user")
def remove_user(user_id: int, admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not isinstance(user, User):
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": "User removed successfully"}


@router.get("/search", tags=["admin"], summary="Search for a user")
def search_user(username: str, admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    users = session.query(User).filter(User.username.ilike(f"%{username}%")).all()
    user_list = [user.__dict__ for user in users]
    return {"users": user_list}


@router.get("/all", tags=["admin"], summary="Get all users")
def get_all_user(admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    users = session.query(User).all()
    return {"data": users}


@router.get("/me", summary="Get your own user data")
def get_me(user: User = Depends(auth_user), session: Session = Depends(get_session)):
    return user.__dict__


@router.patch("/change-password", summary="Change password")
def change_my_password(new_password: str, user: User = Depends(auth_user), session: Session = Depends(get_session)):
    user.set_password(new_password)
    session.commit()
    return {"message": "Password changed successfully"}


@router.post("/check-username", summary="Check if username is available")
def check_username(invite_token: str, username: str, session: Session = Depends(get_session)):
    invite = session.query(Invite).filter(Invite.token == invite_token).first()

    if not isinstance(invite, Invite) or invite.accepted:
        raise HTTPException(status_code=404, detail="Invalid invite token")

    user = session.query(User).filter(User.username == username).first()

    if isinstance(user, User):
        raise HTTPException(status_code=400, detail="Username is not available")

    return {"message": "Username is available"}
