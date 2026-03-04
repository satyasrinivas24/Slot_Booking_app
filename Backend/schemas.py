from pydantic import BaseModel
from typing import Optional

class Slot(BaseModel):
    id: int
    slot_time: str
    status: str
    username: Optional[str]

    class Config:
        from_attributes = True


class BookSlot(BaseModel):
    username: str