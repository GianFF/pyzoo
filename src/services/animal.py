from typing import Union
import src.types.animal as animal
import src.repositories.animal as repository

class AnimalService:
    def __init__(self, repository: repository.AnimalRepository):
        self.repository = repository

    def get_all(self):
        return self.repository.select_all()

    def get_animal(self, animal_id: int, q: Union[str, None] = None):
        return self.repository.select_animal(animal_id)

    def save_animal(self, animal: animal.AnimalType):
        return self.repository.insert_animal(animal.specie, animal.animal_sound)

    def update_animal(self, animal_id: int, animal: animal.AnimalType):
        return animal.animal_id
