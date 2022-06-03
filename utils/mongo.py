from multiprocessing import AuthenticationError
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv
import os


class DataBase:
    mongo_user = os.environ.get("MONGO_USER", None)
    mongo_pwd = os.environ.get("MONGO_PWD", None)
    if not (mongo_pwd and mongo_user):
        raise AuthenticationError(
            "Missing Mongo auth. Please define MONGO_USER and MONGO_PWD in .env"
        )

    def __init__(self) -> None:
        load_dotenv()
        self.conn = MongoClient(
            "mongodb+srv://{}:{}@linq.aybjjlo.mongodb.net/?retryWrites=true&w=majority"
        )
