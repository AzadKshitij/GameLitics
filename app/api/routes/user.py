from typing import Any, List
from venv import logger
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.models.user import User
from app.api import deps
from app.schemas import user

router = APIRouter()


@router.get("/{user_id}")
def read_item(
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve items.
    """
    user_info = db.query(User).filter(
        User.id == user_id).all()
    return jsonable_encoder(user_info)

# @router.post("/", response_model=user.User)
@router.post("/")
def create(db: Session = Depends(deps.get_db)):
        logger.info("Creating user")
        db_obj = User()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj