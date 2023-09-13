import secrets
from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, EmailStr
from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database.orm import Base

"""SQLAlchemy Models"""


class Invite(Base):
    __tablename__ = "invite"

    id: Mapped[Optional[int]] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    invited_by: Mapped[Optional[str]] = mapped_column(ForeignKey('user.username'), nullable=False)
    revoked_by: Mapped[Optional[str]] = mapped_column(ForeignKey('user.username'), nullable=True)
    token: Mapped[Optional[str]] = mapped_column(String(64), insert_default=secrets.token_urlsafe(32), unique=True)
    email: Mapped[str] = mapped_column(String(64), nullable=False, unique=True)
    is_admin: Mapped[bool] = mapped_column(insert_default=False)
    accepted: Mapped[Optional[bool]] = mapped_column(insert_default=False)  # marked if registration completed
    created_at: Mapped[Optional[datetime]] = mapped_column(insert_default=func.now())

    def __init__(self, **kw: Any):
        super().__init__(**kw)


"""Pydantic Models"""


class InvitePost(BaseModel):
    is_admin: bool
    email: EmailStr
