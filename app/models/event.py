from sqlite3 import Timestamp
from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

import datetime



class Event(Base):
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gameName = Column(String, index=True)
    gameVersion  = Column(String, index=True)
    eventDate = Column(DateTime, index=True, default=datetime.datetime.utcnow())
    eventType = Column(String, index=True)
    eventParam = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="event")