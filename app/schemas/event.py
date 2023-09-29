from typing import Optional
from pydantic import BaseModel


# Shared properties
class EventBase(BaseModel):
    gameName: Optional[str] = None
    gameVersion: Optional[str] = None
    eventDate: Optional[str] = None
    eventType: Optional[str] = None
    eventParam: Optional[str] = None



# Properties to receive on Event creation
class EventCreate(EventBase):
    gameName: str
    gameVersion: str
    eventDate: str
    eventType: str
    eventParam: str


# Properties to receive on Event update
class EventUpdate(EventBase):
    pass


# Properties shared by models stored in DB
class EventInDBBase(EventBase):
    id: int
    gameName: str
    gameVersion: str
    eventDate: str
    eventType: str
    eventParam: str
    owner_id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Event(EventInDBBase):
    pass


# Properties properties stored in DB
class EventInDB(EventInDBBase):
    pass