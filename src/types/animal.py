from typing import Union
from pydantic import BaseModel

class AnimalType(BaseModel):
    animal_id: int
    specie: str
    animal_sound: Union[str, None] = None