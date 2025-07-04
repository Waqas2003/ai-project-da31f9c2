from fastapi import APIRouter, Depends, HTTPException
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND
from pydantic import BaseModel
from typing import List
import json
import os

router = APIRouter(prefix="/api")

@router.get("/users/")
async def read_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return JSONResponse(content={"users": users}, media_type="application/json")

@router.post("/users/")
async def create_user(user: UserSchema):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (user.username, user.email, user.password))
    conn.commit()
    conn.close()
    return JSONResponse(status_code=HTTP_201_CREATED, content={"message": "User created successfully"}, media_type="application/json")

@router.get("/products/")
async def read_products():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return JSONResponse(content={"products": products}, media_type="application/json")

@router.post("/products/")
async def create_product(product: ProductSchema):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price, image) VALUES (?, ?, ?, ?)", (product.name, product.description, product.price, product.image))
    conn.commit()
    conn.close()
    return JSONResponse(status_code=HTTP_201_CREATED, content={"message": "Product created successfully"}, media_type="application/json")

@router.get("/orders/")
async def read_orders():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return JSONResponse(content={"orders": orders}, media_type="application/json")

@router.post("/orders/")
async def create_order(order: OrderSchema, user: User = Depends()):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (user_id, product_id, quantity, total) VALUES (?, ?, ?, ?)", (user.id, order.product_id, order.quantity, order.total))
    conn.commit()
    conn.close()
    return JSONResponse(status_code=HTTP_201_CREATED, content={"message": "Order created successfully"}, media_type="application/json")