from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
load_dotenv() 

user = "postgres"
password = "senha"
database = "pds"
host = "localhost"

# user = os.getenv("USER")
# password = os.getenv("PASSWORD")
# host = os.getenv("HOST")
# database = os.getenv("DATABASE")


SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush= False, bind= engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
