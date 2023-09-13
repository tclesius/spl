from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import String, Text, func, ForeignKey, CheckConstraint
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from database.orm import Base

"""SQLAlchemy Model"""


class Release(Base):
    __tablename__ = "release"
    id: Mapped[int] = mapped_column(primary_key=True)
    subdivision_id: Mapped[int] = mapped_column(ForeignKey("subdivision.id"))
    added_by_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    title: Mapped[str] = mapped_column(Text())
    producers: Mapped[str] = mapped_column(Text())  # mapping will be handled via substring search
    artists: Mapped[str] = mapped_column(Text())  # mapping will be handled via substring search
    cover: Mapped[str] = mapped_column(Text())  # filename on fileserver
    spotify_url: Mapped[str] = mapped_column(Text(), nullable=True)
    soundcloud_url: Mapped[str] = mapped_column(Text(), nullable=True)
    release_year: Mapped[int] = mapped_column()
    release_type: Mapped[str] = mapped_column(String(6))
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.now()
    )

    subdivision_rel = relationship("Subdivision", back_populates="release_rel")
    added_by_user_rel = relationship("User", back_populates="release_rel")
    # check that release type is either "album" or "single"
    __table_args__ = (
        CheckConstraint(release_type.in_(["album", "single"])),
    )

    def __init__(self, **kw):
        super().__init__(**kw)


"""Pydantic Model"""


class ReleaseBase(BaseModel):
    ...


class ReadRelease(ReleaseBase):
    ...


class CreateRelease(ReleaseBase):
    title: str
    producers: str
    artists: str
    subdivision: int
    cover: str
    spotify_url: Optional[str] = None
    soundcloud_url: Optional[str] = None
    release_year: int
    release_type: str
