from typing import Annotated

from pydantic import BaseModel, StringConstraints, Field, ConfigDict

titleStr = Annotated[str, StringConstraints(min_length = 2, max_length = 100)]
authorStr = Annotated[str, StringConstraints(min_length = 2, max_length = 50)]
isbnStr = Annotated[str, StringConstraints(pattern = r"^978\d{10}$")]


class BookCreate(BaseModel):
    title : titleStr
    author : authorStr
    isbn : isbnStr
    year : int = Field(gt = 1450, lt = 2027)


class BookReading(BaseModel):
    model_config = ConfigDict(from_attributes = True)
    id:int
    title : titleStr
    author : authorStr
    isbn : isbnStr
    year:int

