from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from api.model import Product
from api.database import sessionLocal, create_tables
import api.crud as crud

app = FastAPI()

create_tables()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# Home
@app.get("/")
async def root():
    return {"message": "Welcome to the Product API"}

# Get all products
@app.get("/products", response_model=list[Product])
async def get_products(db: Session = Depends(get_db)):
    data = [x.__dict__ for x in crud.get_all_products(db)]
    return data

# Get product by ID
@app.get("/products/{product_id}", response_model=Product)
async def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product  # FastAPI will handle the conversion

# Create product
@app.post("/products", response_model=Product)
async def add_new_product(product: Product, db: Session = Depends(get_db)):
    db_product = crud.create_product(db, product)
    return db_product

# Update product
@app.put("/products/{product_id}", response_model=Product)
async def update_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):
    updated = crud.update_product(db, product_id, updated_product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

# Delete product
@app.delete("/products/{product_id}", response_model=Product)
async def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
    deleted_product = crud.delete_product(db, product_id)
    if not deleted_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product