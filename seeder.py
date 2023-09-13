from alembic import command
from alembic.config import Config
from sqlalchemy.orm import Session

from database.orm import SessionLocal
from producer.model import Producer
from release.model import Release
from social.model import Social
from subdivision.model import Subdivision
from user.model import User


def seed_user(session: Session):
    session.add_all([
        User(
            id=1,
            is_admin=True,
            username="admin",
            email="admin@admin.com",
            password="admin"
        ),
        User(
            id=2,
            is_admin=False,
            username="test",
            email="test@test.com",
            password="test"
        ),

    ])


def seed_subdivision(session: Session):
    session.add_all([
        Subdivision(
            id=1,
            country="france"
        ),
        Subdivision(
            id=2,
            country="germany"
        ),
        Subdivision(
            id=3,
            country="america"
        ),
        Subdivision(
            id=4,
            country="united kingdom"
        ),
    ])


def seed_social(session: Session):
    session.add_all([
        Social(
            id=1,
            spotify_url="https://open.spotify.com/artist/0Y5tJX1MQlPlqiwlOH1tJY",
            soundcloud_url="https://soundcloud.com/officialmedasin",
            instagram_url="https://www.instagram.com/medasin.music/"
        )
    ])


def seed_producer(session: Session):
    session.add_all([
        Producer(
            id=1,
            name="mario",
            subdivision=1,
            picture="default.png",
            social=1,
            aliases="topg,noluigi"
        ),
        Producer(
            id=2,
            name="luigi",
            subdivision=1,
            social=1,
            picture="default.png",
            aliases="lui,peacher,bowserado"
        ),
    ])


def seed_release(session: Session):
    session.add_all([
        Release(
            id=1,
            added_by_id=1,
            title="mario",
            subdivision_id=1,
            producers="mario,luigi",
            artists="bowser feat. peach",
            cover="default.png",
            spotify_url="https://open.spotify.com/album/1DFixLWuPkv3KT3TnV35m3",
            soundcloud_url="https://soundcloud.com/officialmedasin/daydream-ft-joba",
            release_year=2020,
            release_type="album",
        ),
        Release(
            id=2,
            added_by_id=2,
            title="marr",
            subdivision_id=1,
            producers="todd,luigi",
            artists="bowser feat. peach",
            cover="default.png",
            spotify_url="https://open.spotify.com/album/1DFixLWuPkv3KT3TnV35m3",
            soundcloud_url="https://soundcloud.com/officialmedasin/daydream-ft-joba",
            release_year=2020,
            release_type="album",
        )
    ])


def seed_database():
    with SessionLocal() as session:
        alembic_cfg = Config("alembic.ini")
        command.downgrade(alembic_cfg, "base")
        command.upgrade(alembic_cfg, "head")

        seed_user(session)
        seed_subdivision(session)
        seed_social(session)
        seed_producer(session)
        seed_release(session)
        session.commit()


if __name__ == "__main__":
    seed_database()
