from database import Base
from sqlalchemy import Column, Integer, LargeBinary


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer(), primary_key=True)
    data = Column(LargeBinary(length=128))