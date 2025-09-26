from pydantic import BaseModel, ConfigDict

class FruitCreate(BaseModel):
    name: str
    seedless: bool = True 

class FruitRead(FruitCreate):
    id: int 
    # class Config:
    #     orm_mode = True 

    model_config = ConfigDict(from_attributes=True)