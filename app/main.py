from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.models import Base, BookDB
from app.schemas import BookCreate, BookReading

Base.metadata.create_all(bind = engine)

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}


@app.post("/api/books", response_model = BookReading, status_code = status.HTTP_201_CREATED)
def add_book_id(new_book:BookCreate, db:Session = Depends(get_db)):
    db_book = BookDB(**new_book.model_dump())
    db.add(db_book)
    try:
        db.commit();
        db.refresh(db_book)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail= "A book with the same isbn already exists")
    return db_book
@app.get("/api/books", response_model = list[BookReading])
def get_books(db:Session = Depends(get_db)):
    statement = Select (BookDB).order_by(BookDB.id)
    return
    db.execute(statement).scalars().all()

@app.get("/api/books/{book_id}")
def get_books(book_id:int, db:Session = Depends(get_db)):
    db_book = db.get(BookDB, book_id)
    if db_book is none:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")
        return db_book


@app.delete("/api/books/{book_id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db.book = db.get(BookDB, book_id)
    if db.book is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")
        db.delete (db_book)
        db.commit()
        return
    

