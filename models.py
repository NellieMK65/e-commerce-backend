# from sqlalchemy.orm import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, VARCHAR, ForeignKey, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# import sqlite3

# conn = sqlite3.connect('e-commerce.db')

# cursor = conn.cursor()

# 1. create an engine that connects to our db
engine = create_engine('sqlite:///e-commerce.db', echo = True)

# 2. create a session
Session = sessionmaker(bind=engine)

# 3. for fastapi, we need to create a method/function that returns the session
def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()

# Create a base class
# class Base(DeclarativeBase):
#     pass
Base = declarative_base()
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



