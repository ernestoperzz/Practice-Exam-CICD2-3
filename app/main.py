from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Sessio
from app.database import engine, get_db
from app.models import Base, BookDB
from app.schemas import BookCreate, BookReading

Base.metadata.create_all(bind = engine)

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}


@app.post("/api/books", response_model = BookReading, status_code = status.HTTP_201_CREATED)
def add_book_id(new_book_id:BookCreate, db:Session = Depends(get_db)):
    db_book = BookDB(**new_book_dump())
    db.add(db_book)
    try:
        db.commit;
db.refresh(db_book)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail= " A book with the same isbn already exists")
        return db_book

