from typing import List
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from .database import SessionLocal #
from .database import get_db #
from sqlalchemy.orm import Session
from . import models #
from .models import Fruit #
from .schemas import FruitCreate, FruitRead #
from fastapi import status


# FastAPI app
app = FastAPI()

# Pydantic Class - Represents an entity 
class Fruit(BaseModel):
    name: str
    seedless: bool = True

# fruits = []

# Endpoint 1
@app.get("/")
def index():
    return {"message": "Welcome to Spixah Sonic API"}

# Post Fruit
@app.post("/new", response_model=FruitRead, status_code=status.HTTP_201_CREATED)
def create(fruit: FruitCreate, db: Session = Depends(get_db)):
    new_fruit = models.Fruit(name=fruit.name, seedless=fruit.seedless)
    db.add(new_fruit) 
    db.commit()
    db.refresh(new_fruit)
    return new_fruit


# Get Fruits
@app.get("/fruits", response_model=List[FruitRead])
def get_fruits(db: Session = Depends(get_db)):
    fruits = db.query(models.Fruit).all()
    return fruits

# Get Fruit By ID 
@app.get("/fruits/{fruit_id}", response_model=FruitRead)
def get_fruit(fruit_id: int, db: Session = Depends(get_db)):
    fruit = db.query(models.Fruit).filter(models.Fruit.id == fruit_id).first()
    if not fruit:
        raise HTTPException(status_code=404, detail="Fruit not found")
    return fruit

# Update Fruit By ID 
@app.put("/fruits/{fruit_id}", response_model=FruitRead, status_code=status.HTTP_200_OK)
def update_fruit(fruit_id: int, fruit_in: FruitCreate, db: Session = Depends(get_db)):
    fruit_db = db.query(models.Fruit).get(fruit_id)
    if not fruit_db:
        raise HTTPException(status_code=404, detail="Fruit not found")
    fruit_db.name = fruit_in.name
    fruit_db.seedless = fruit_in.seedless 
    db.commit()
    db.refresh(fruit_db)
    return fruit_db





# # Endpoint 3
# @app.get("/fruits", response_model=list[FruitCreate])
# def get_fruits():
#     return fruits

# # Endpoint 4
# @app.get("/fruits/{fruit_index}", response_model=FruitCreate)
# def get_fruit(fruit_index: int) -> FruitCreate:
#     if (0 <= fruit_index < len(fruits)):
#         return fruits[fruit_index]
#     else:
#         raise HTTPException(status_code=404, detail="Fruit not found")


##
# uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
##

##
# uvicorn main:app --reload --app-dir app --host 127.0.0.1 --port 8000
##