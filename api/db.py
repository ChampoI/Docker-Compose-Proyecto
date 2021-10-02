import os
from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connection_db = f'postgresql://{user}:{password}@{host}:{port}/{database}'

connection_db = 'postgresql://hello_flask:hello_flask@db:5432/hello_flask_dev'
engine = create_engine(connection_db)
meta = MetaData()

conn = engine.connect()
