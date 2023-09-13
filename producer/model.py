from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import func, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.orm import Base
from social.model import SocialBase


class Producer(Base):
    __tablename__ = "producer"
    id: Mapped[int] = mapped_column(primary_key=True)
    social: Mapped[int] = mapped_column(ForeignKey("social.id"))
    subdivision: Mapped[int] = mapped_column(ForeignKey("subdivision.id"))
    picture: Mapped[str] = mapped_column(Text())  # filename on fileserver
    name: Mapped[str] = mapped_column(Text())
    aliases: Mapped[str] = mapped_column(Text())
    bio: Mapped[str] = mapped_column(Text(), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        insert_default=func.now()
    )

    subdivision_rel = relationship("Subdivision", back_populates="producer_rel")
    social_rel = relationship("Social", back_populates="producer_rel")

    def __init__(self, **kw):
        super().__init__(**kw)


class ProducerCreate(BaseModel):
    name: str
    socials: SocialBase
    aliases: list[str]
    subdivision: int
    bio: str | None = None
    picture: str = "default.png"
