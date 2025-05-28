# import fastapi package
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import get_db, Product, Category
from schemas import ProductSchema, CategorySchema

# initialize it
app = FastAPI()

# allow network request from all servers
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])


# define routes
@app.get("/")
def index():
    return {"message": "Welcome to my first backend app"}


# products
# http://localhost:8000/products -> GET -> gets all products
@app.get("/products")
def products(session: Session = Depends(get_db)):
    # retrieves all products from the table
    products = session.query(Product).all()
    # categories = session.query(Category).all()
    # use sqlalchemy to retrieve all products from the db
    return products


def sum(a: int, b: int = 8):
    return a + b


# http://localhost:8000/products -> POST -> create a single product
@app.post("/products")
def add_product(product: ProductSchema, db: Session = Depends(get_db)):
    # 1. Create an instance of the product model with the values sent
    # new_product = Product(
    #     name=product.name,
    #     price=product.price,
    #     image=product.image,
    #     category_id=product.category_id,
    # )
    new_product = Product(**product.model_dump())

    # 2. Add the product the transaction
    db.add(new_product)
    # 3. commit the transaction
    db.commit()

    return {"message": "Product created successfully"}


# http://localhost:8000/products/3 -> GET -> get a single product
@app.get("/products/{id}")
def get_product(id: int):
    print("Product id", id)
    return {}


# http://localhost:8000/products/3 -> PATCH/PUT -> update a single product
@app.patch("/products/{id}")
def update_product(id: int):
    print(f"Product of id {id} updated")
    return {"message": "Product updated successfully"}


# http://localhost:8000/products/3 -> DELETE -> delete a single product
@app.delete("/products/{id}")
def delete_product(id):
    print(f"Product of id {id} deleted")
    # runnig an sql with DELETE
    # run an update operation and set deleted_at/is_deleted column
    return {"message": "Product deleted successfully"}


# categories
# create a category
@app.post("/category")
def add_category(category: CategorySchema, db: Session = Depends(get_db)):
    new_category = Category(**category.model_dump())

    db.add(new_category)

    db.commit()

    return {"message": "Category created successfully"}


@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()

    return categories
