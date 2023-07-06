from sqlalchemy import Table, Column, Integer, String, MetaData

from src.db.connection import engine

metadata_obj = MetaData()

animal_table = Table(
    "animal",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("specie", String(30)),
    Column("animal_sound", String),
)

# metadata_obj.create_all(bind=engine)

# from sqlalchemy import select, insert

# stmt = insert(animal_table).values(animal_sound="grr", specie="Lion")
# with engine.connect() as conn:
#     result = conn.execute(stmt)
#     conn.commit()

# stmt = select(animal_table)
# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)
