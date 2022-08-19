from typing import Optional

from pydantic import BaseModel


class DataObject(BaseModel):
    data: str

    class Config:
        orm_mode = True

class DateInput(BaseModel):
    data: bytes