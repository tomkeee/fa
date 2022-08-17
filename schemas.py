from typing import Optional

from pydantic import BaseModel


class DataObject(BaseModel):
    id: Optional[int]
    username: str

    class Config:
        orm_mode = True


class DataInput(BaseModel):
    id: Optional[int]
    username: Optional[str]
    email: Optional[str]
