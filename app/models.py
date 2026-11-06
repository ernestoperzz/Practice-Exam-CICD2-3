from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class BookDB(base):
    __tableName__="books";
    id:Mapped[int] = mapped_column(Integer, primary key = True, index = True)
    title: Mapped[str] = mapped_column(String(100), nullable = False)
    author: Mapped[str] = mapped_column(String(50), nullable = False) 
    isbn: Mapped[str] = mapped_column(String(13), unique = True, nullable = False)
    year: Mapped[int] = mapped_column(Integer, nullable = False)