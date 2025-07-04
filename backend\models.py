from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str

class Product(BaseModel):
    id: int
    name: str
        price: float
    image: str

class Order(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total: float