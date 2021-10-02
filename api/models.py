from sqlalchemy import Column, String, Integer,Float,DateTime,Text
from sqlalchemy.schema import ForeignKey
from db import engine
from sqlalchemy.orm import sessionmaker, relationship
import datetime

from sqlalchemy import Column, Table
from db import meta, engine
'''
        data["first_name"] = fake.first_name()
        data["day_of_month"] = fake.day_of_month()
        data["day_of_week"] = fake.day_of_week()
        data["country"] = fake.country()
        data["word"] = fake.word()

'''
datos_falsos = Table(
    "datos_falsos",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "first_name",
        String(255),
    ),
    Column("day_of_month", String(255)),
    Column("day_of_week", String(255)),
    Column("country", String(255)),
    Column("word", String(255)),
)

meta.create_all(engine)
