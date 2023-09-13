from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from auth.service import auth_admin
from database.dependency import get_session
from producer.model import Producer, ProducerCreate
from social.model import Social
from user.model import User

router = APIRouter(prefix="/producer", tags=["producer"])


@router.get("/all")
def get_all_producer(session: Session = Depends(get_session)):
    producers = session.query(Producer).all()
    return {"data": producers}


@router.post("/create", tags=["admin"])
def create_producer(producer: ProducerCreate, admin: User = Depends(auth_admin),
                    session: Session = Depends(get_session)):
    producer = producer.model_dump()
    social = producer.pop("socials")
    social = Social(**social)
    session.add(social)
    session.commit()
    producer = Producer(**producer, social=social.id)
    session.add(producer)
    session.commit()
    return {"message": "Producer created successfully"}


@router.delete("/remove", tags=["admin"])
def delete_producer(producer_id: int, admin: User = Depends(auth_admin), session: Session = Depends(get_session)):
    producer = session.get(Producer, producer_id)
    if not isinstance(producer, Producer):
        raise HTTPException(status_code=404, detail="Producer not found")
    session.delete(producer)
    session.commit()
    return {"message": "Producer removed successfully"}


@router.patch("/change", tags=["admin"])
def change_producer(producer_id: int, producer: ProducerCreate, admin: User = Depends(auth_admin),
                    session: Session = Depends(get_session)):
    producer_db = session.get(Producer, producer_id)
    if not isinstance(producer_db, Producer):
        raise HTTPException(status_code=404, detail="Producer not found")
    producer = producer.model_dump()
    social = producer.pop("socials")
    social = Social(**social)
    session.add(social)
    session.commit()
    producer_db = Producer(**producer, social=social.id)
    session.add(producer_db)
    session.commit()
    return {"message": "Producer changed successfully"}


@router.get("/search", tags=["admin"])
def search_producer(q: str, session: Session = Depends(get_session), admin: User = Depends(auth_admin)):
    producers = session.query(Producer).filter(
        or_(
            Producer.name.ilike(f"%{q}%"),
            Producer.aliases.ilike(f"%{q}%")
        )
    ).all()
    return {"data": producers}
