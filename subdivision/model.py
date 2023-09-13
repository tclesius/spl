from datetime import datetime
from typing import Any

from pydantic import BaseModel
from sqlalchemy import func, String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.orm import Base
from social.model import SocialBase


class Subdivision(Base):
    __tablename__ = "subdivision"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    social: Mapped[int] = mapped_column(ForeignKey("social.id"), nullable=True)
    country: Mapped[str] = mapped_column(String(32))
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.now()
    )
    social_rel = relationship("Social", back_populates="subdivision_rel")
    producer_rel = relationship("Producer", back_populates="subdivision_rel")
    release_rel = relationship("Release", back_populates="subdivision_rel")

    def __init__(self, **kw: Any):
        super().__init__(**kw)


class SubdivisionBase(BaseModel):
    country: str
    socials: SocialBase
    picture: str = "default.png"
