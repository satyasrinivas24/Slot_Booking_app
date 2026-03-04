from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# this react connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# View available slots
@app.get("/slots", response_model=list[schemas.Slot])
def get_slots(db: Session = Depends(get_db)):

    slots = db.query(models.Slot).filter(models.Slot.status == "available").all()

    return slots


# Book slot
@app.post("/book/{slot_id}")
def book_slot(slot_id: int, data: schemas.BookSlot, db: Session = Depends(get_db)):

    slot = db.query(models.Slot).filter(models.Slot.id == slot_id).first()

    if not slot:
        raise HTTPException(status_code=404, detail="Slot not found")

    if slot.status == "booked":
        raise HTTPException(status_code=400, detail="Slot already booked")

    slot.status = "booked"
    slot.username = data.username

    db.commit()

    return {"message": "Slot booked successfully"}


# View booked slots
@app.get("/booked", response_model=list[schemas.Slot])
def booked_slots(db: Session = Depends(get_db)):

    slots = db.query(models.Slot).filter(models.Slot.status == "booked").all()

    return slots