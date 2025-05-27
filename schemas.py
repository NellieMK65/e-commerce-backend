# Its going to contain classes acting as blueprint for post/patch methods
from pydantic import BaseModel


class ProductSchema(BaseModel):
    name: str
    price: int
    image: str
    category_id: int


class CategorySchema(BaseModel):
    name: str
