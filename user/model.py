from dataclasses import InitVar
from datetime import datetime
from typing import Any

from passlib.hash import pbkdf2_sha256
from pydantic import BaseModel
from sqlalchemy import String, func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.orm import Base


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement='auto',
        nullable=False)  # TODO change to uuid https://stackoverflow.com/questions/183042/how-can-i-use-uuids-in-sqlalchemy
    is_admin: Mapped[bool] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    password: InitVar[str]
    password_hash: Mapped[str] = mapped_column(String(128), init=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())

    # TODO should use Cryptcontext for automatic refresh of hashes if depr
    def __init__(self, is_admin, username, email, password, **kw: Any):
        super().__init__(**kw)
        self.is_admin = is_admin
        self.username = username
        self.email = email
        self.set_password(password)  # Automatically hash the password

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password_hash)

    def set_password(self, password):
        self.password_hash = pbkdf2_sha256.hash(password)

    release_rel = relationship("Release", back_populates="added_by_user_rel")


"""Pydantic Model"""


class UserBase(BaseModel):
    ...


class UserRelease(UserBase):
    ...
