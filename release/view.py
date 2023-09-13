from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from auth.service import auth_user, auth_admin
from database.dependency import get_session
from release.model import Release, CreateRelease
from user.model import User

router = APIRouter(prefix="/release", tags=["release"])


@router.get("/all", tags=["admin"], dependencies=[Depends(auth_admin)])
async def get_all(session: Session = Depends(get_session)) -> dict:
    releases = session.query(Release).all()
    return {"data": releases}


@router.get("/latest", dependencies=[Depends(auth_user)])
def get_latest_release(session: Session = Depends(get_session)):
    release = session.query(Release).order_by(Release.id.desc()).first()
    return {"data": release}


@router.post("/create", tags=["admin"], dependencies=[Depends(auth_admin)])
def create_release(release: CreateRelease = Depends(), admin: User = Depends(auth_admin),
                   session: Session = Depends(get_session)):
    release_db = Release(**release.model_dump(), added_by=admin.id)
    session.add(release_db)
    session.commit()
    return {"message": "Release created successfully"}


# @router.patch("/change", tags=["admin"], dependencies=[Depends(auth_admin)])
# def change_release(release_id: int,
#                    release: ChangeRelease,
#                    session: Session = Depends(get_session)):
#     release = session.get(Release, release_id)
#     if not isinstance(release, Release):
#         raise HTTPException(status_code=404, detail="Release not found")
#     release = Release(**release.model_dump())
#     session.add(release)
#     session.commit()
#
#     return {"message": "Release changed successfully"}


@router.delete("/remove", tags=["admin"], dependencies=[Depends(auth_admin)])
def remove_release(release_id: int, session: Session = Depends(get_session)):
    release = session.get(Release, release_id)
    if not isinstance(release, Release):
        raise HTTPException(status_code=404, detail="Release not found")
    session.delete(release)
    session.commit()
    return {"message": "Release removed successfully"}


@router.get("/search", tags=["admin"], dependencies=[Depends(auth_admin)])
def search_release(q: str, session: Session = Depends(get_session)):
    releases = (session.query(Release).join(Release.added_by_user_rel).filter(
        or_(
            Release.title.ilike(f"%{q}%"),
            Release.artists.ilike(f"%{q}%"),
            Release.producers.ilike(f"%{q}%"),
            User.username.ilike(f"%{q}%")
        ),
    ).all())
    return {"releases": releases}
