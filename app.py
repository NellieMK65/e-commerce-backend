# import fastapi package
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import get_db, Product, Category

# initialize it
app = FastAPI()

# allow network request from all servers
app.add_middleware(CORSMiddleware, allow_origins=["*"])

# define routes
@app.get('/')
def index():
    return { "message": "Welcome to my first backend app" }

# products
# http://localhost:8000/products -> GET -> gets all products
@app.get('/products')
def products(session = Depends(get_db)):
    # retrieves all products from the table
    products = session.query(Product).all()
    # categories = session.query(Category).all()
    # use sqlalchemy to retrieve all products from the db
    return products

# http://localhost:8000/products -> POST -> create a single product
@app.post('/products')
def add_product():
    return { "message": "Product created successfully" }

# http://localhost:8000/products/3 -> GET -> get a single product
@app.get('/products/{id}')
def get_product(id: int):
    print("Product id", id)
    return {}

# http://localhost:8000/products/3 -> PATCH/PUT -> update a single product
@app.patch('/products/{id}')
def update_product(id: int):
    print(f"Product of id {id} updated")
    return { "message": "Product updated successfully" }

# http://localhost:8000/products/3 -> DELETE -> delete a single product
@app.delete('/products/{id}')
def delete_product(id):
    print(f"Product of id {id} deleted")
    # runnig an sql with DELETE
    # run an update operation and set deleted_at/is_deleted column
    return { "message": "Product deleted successfully" }



# categories
