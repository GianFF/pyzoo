from typing import Union
from fastapi import FastAPI
import src.types.animal as animal
import src.services.animal as service
import src.repositories.animal as repository
from src.db.models import metadata_obj
from src.db.connection import engine

def dependencies():
    metadata_obj.create_all(engine)
    animal_repository = repository.AnimalRepository(engine)
    animal_service = service.AnimalService(animal_repository)
    return animal_service

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/animals")
def get_all():
    animal_service = dependencies()
    return {"animals": animal_service.get_all()}


@app.get("/animals/{animal_id}")
def get_animal(animal_id: int, q: Union[str, None] = None):
    animal_service = dependencies()
    return {"animal_id": animal_service.get_animal(animal_id, q), "q": q}


@app.post("/animals/")
def save_animal(the_animal: animal.AnimalType):
    animal_service = dependencies()
    return {"animal_id": animal_service.save_animal(the_animal)}


@app.put("/animals/{animal_id}")
def update_animal(animal_id: int, animal: animal.AnimalType):
    animal_service = dependencies()
    return {"animal_id": animal_service.update_animal(animal_id, animal)}