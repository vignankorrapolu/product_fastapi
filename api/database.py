from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.model import Product_Database
from os import getenv


DATABASE_URL = getenv("DATABASE_URL", "sqlite:///./test.db")

engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})
sessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)


def create_tables():
    Product_Database.metadata.create_all(bind=engine)
