from fastapi import FastAPI, HTTPException
from typing import List
from api.model import product
from api.database import products

app = FastAPI()

# Home
@app.get("/")
async def root():
    return {"message": "Welcome to the Product API"}

# Get all products
@app.get("/products", response_model=List[product])
async def get_products():
    return products

# Get product by ID
@app.get("/products/{product_id}", response_model=product)
async def get_product_by_id(product_id: int):
    for item in products:
        if item.id == product_id:
            return item  
    raise HTTPException(status_code=404, detail="product ID not found")


# Create product
@app.post("/products", response_model=product)
async def add_new_product(product: product):
    for item in products:
        if item.id == product.id:
            raise HTTPException(status_code=400, detail="Product with this ID already exists")
    products.append(product)
    return product


# Update product
@app.put("/products/{product_id}", response_model=product)
async def update_product(product_id: int, updated_product: product):
    for index, p in enumerate(products):
        if p.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product_id not found")

# Delete product
@app.delete("/products/{product_id}")
async def delete_product_by_id(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            deleted = products.pop(i)
            return {product_id: "Product deleted successfully"}
    raise HTTPException(status_code=404, detail="Product ID not found")

