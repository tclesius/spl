import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, sessionmaker

from settings import settings

engine = create_engine(settings.POSTGRES_DB_URL)
SessionLocal = sessionmaker(engine)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


class Base(MappedAsDataclass, DeclarativeBase):
    pass
