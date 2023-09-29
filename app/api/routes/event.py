from typing import Any, List
from venv import logger
from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.models.event import Event
from app.api import deps
from app.schemas import event

router = APIRouter()


@router.get("/{owner_id}", response_model=event.Event)
def read_items(
    owner_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Retrieve items.
    """
    # db.query(Event).filter(Event.owner_id == owner_id).all()
    return db.query(Event).filter(Event.owner_id == owner_id).all()



@router.post("/{owner_id}", response_model=event.Event)
def create_item(
    owner_id: int,
    obj_in: event.EventCreate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Create new item.
    """
    obj_in_data = jsonable_encoder(obj_in)
    db_obj = Event(**obj_in_data, owner_id=owner_id)
    try:
        logger.info("Creating event")
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
    except Exception as e:
        logger.error(e)
        raise e
    return db_obj



@router.put("/{id}", response_model=event.Event)
def update_item(
    owner_id: int,
    id: int,
    obj_in: event.EventUpdate,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Update an item.
    """
    obj_in_data = jsonable_encoder(obj_in)
    db_obj = db.query(Event).filter(Event.owner_id == owner_id).filter(Event.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="Item not found")
    update_data = obj_in_data
    for field in db_obj:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


@router.delete("/{id}", response_model=event.Event)
def delete_item(
    owner_id: int,
    id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete an item.
    """
    db_obj = db.query(Event).filter(Event.owner_id == owner_id).filter(Event.id == id).first()
    if not db_obj:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_obj)
    db.commit()
    return db_obj