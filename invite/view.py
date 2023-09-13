from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.service import auth_admin
from database.dependency import get_session
from invite.model import Invite, InvitePost
from invite.service import send_email
from user.model import User

router = APIRouter(prefix="/invite", tags=["invite"])


@router.post("/revoke", tags=["admin"], summary="Revoke an invite")
def revoke(invite_id: int, admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    invite = session.get(Invite, invite_id)
    if not isinstance(invite, Invite):
        raise HTTPException(status_code=404, detail="Invite not found")
    invite.revoked_by = admin.username
    session.commit()


@router.post("/send", tags=["admin"], summary="Invite a user")
def send(form: InvitePost, admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    invite_obj = Invite(invited_by=admin.username, email=form.email, is_admin=form.is_admin)
    session.add(invite_obj)
    session.commit()
    send_email(invite_obj)


@router.post("/resend", tags=["admin"], summary="Resend an invite")
def resend(invite_id: int, admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    invite_obj = session.get(Invite, invite_id)
    if not isinstance(invite_obj, Invite):
        raise HTTPException(status_code=404, detail="Invite not found")
    send_email(invite_obj)
