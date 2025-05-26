from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text

# Create a base class
class Base(DeclarativeBase):
    pass

"""
1. We must provide the table via the __tablename__ attribute
2. It must have at least one column defined
"""
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer(), primary_key = True)
    name = Column(Text())
    price = Column(Integer())


