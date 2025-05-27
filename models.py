from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from datetime import datetime

# Create a base class
class Base(DeclarativeBase):
    pass

"""
1. We must provide the table via the __tablename__ attribute
2. It must have at least one column defined
"""
class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    name = Column(Text, unique = True)
    created_at = Column(DateTime, default = datetime.now())

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer(), primary_key = True)
    name = Column(Text())
    price = Column(Integer())
    image = Column(Text)
    category_id = Column(Integer(), ForeignKey("categories.id"))
    created_at = Column(DateTime, default = datetime.now())



