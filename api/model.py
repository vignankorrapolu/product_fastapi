from pydantic import BaseModel, conint
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product_Database(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    price = Column(Float)

# For API requests, make id optional since it will be auto-generated
class Product(BaseModel):
    id: int | None = None
    name: str
    price: int

    class Config:
        orm_mode = True
        from_attributes = True

