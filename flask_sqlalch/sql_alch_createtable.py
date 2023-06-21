from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, insert
from sqlalchemy import MetaData

engine = create_engine("sqlite:///deneme.db",echo=True)
metadata_obj = MetaData()

user_table = Table(
    "user_account_2",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(30)),
    Column("fullname", String),
)

metadata_obj.create_all(engine)

stmt = insert(user_table).values(name="spongebob",fullname="sponge squarepants")

print("PRINT",stmt)

complied = stmt.compile()
print(complied.params)

with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()