from sqlalchemy import Column, Integer, String
from database import Base

class Slot(Base):

    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    slot_time = Column(String(50))
    status = Column(String(20), default="available")
    username = Column(String(100), nullable=True)