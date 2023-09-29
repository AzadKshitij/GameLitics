from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Event(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gameName = Column(String, index=True)
    gameVersion  = Column(String, index=True)
    eventDate = Column(String, index=True)
    eventType = Column(String, index=True)
    eventParam = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="event")