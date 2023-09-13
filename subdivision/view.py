from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth.service import auth_admin
from database.dependency import get_session
from social.model import Social
from subdivision.model import Subdivision, SubdivisionBase
from user.model import User

router = APIRouter(prefix="/subdivision", tags=["subdivision"])


@router.get("/all", tags=["admin"])
def get_all_subdivision(admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    subdivisions = session.query(Subdivision).all()
    return {"data": subdivisions}


@router.delete("/remove", tags=["admin"])
def delete_subdivision(subdivision_id: int, admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    subdivision = session.get(Subdivision, subdivision_id)
    if not isinstance(subdivision, Subdivision):
        raise HTTPException(status_code=404, detail="Subdivision not found")
    session.delete(subdivision)
    session.commit()
    return {"message": "Subdivision removed successfully"}


@router.patch("/change", tags=["admin"])
def change_subdivision(subdivision_id: int, subdivision: SubdivisionBase, admin: User = Depends(auth_admin),
                       session: Session = Depends(get_session)):
    subdivision_db = session.get(Subdivision, subdivision_id)
    if not isinstance(subdivision_db, Subdivision):
        raise HTTPException(status_code=404, detail="Subdivision not found")

    subdivision = subdivision.model_dump()
    social = subdivision.pop("socials")
    social = Social(**social)
    session.add(social)
    session.commit()
    subdivision_db = Subdivision(**subdivision, social=social.id)
    session.add(subdivision_db)
    session.commit()
    return {"message": "Subdivision changed successfully"}
