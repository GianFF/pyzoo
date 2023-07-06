from sqlalchemy import insert, select
from src.db.models import animal_table

class AnimalRepository:
    def __init__(self, engine):
        self.engine = engine

    def insert_animal(self, specie, animal_sound):
        stmt = insert(animal_table).values([{'animal_sound': animal_sound, 'specie': specie}])
        print(stmt)
        with self.engine.connect() as conn:
            result = conn.execute(stmt)
            conn.commit()
        return result

    def select_animal(self, animal_id):
        stmt = select(animal_table).where(animal_table.c.animal_id == animal_id)
        print(stmt)
        result = []
        with self.engine.connect() as conn:
            for row in conn.execute(stmt):
                result.append(row)
                print(row)
        return result

    def select_all(self):
        stmt = select(animal_table)
        print(stmt)
        result = []
        with self.engine.connect() as conn:
            for row in conn.execute(stmt):
                result.append(row)
                print(row)
        return result
