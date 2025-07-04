from pydantic import BaseModel
from typing import List

class UserSchema(BaseModel):
    username: str
    email: str
    password: str

class ProductSchema(BaseModel):
    name: str
        price: float
    image: str

class OrderSchema(BaseModel):
    product_id: int
    quantity: int