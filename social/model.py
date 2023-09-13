from pydantic import BaseModel
from sqlalchemy import Text
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database.orm import Base


class Social(Base):
    __tablename__ = "social"
    # can be mapped to a producer or subdivision
    id: Mapped[int] = mapped_column(primary_key=True)
    spotify_url: Mapped[str] = mapped_column(Text())
    soundcloud_url: Mapped[str] = mapped_column(Text())
    instagram_url: Mapped[str] = mapped_column(Text())

    subdivision_rel = relationship("Subdivision", back_populates="social_rel")
    producer_rel = relationship("Producer", back_populates="social_rel")

    def __init__(self, **kw):
        super().__init__(**kw)


class SocialBase(BaseModel):
    spotify_url: str | None
    soundcloud_url: str | None
    instagram_url: str | None
