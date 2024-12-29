from pymongo import MongoClient

from app.config.config import Config


def get_db_connection():
    client = MongoClient(Config.MONGO_URL)
    db = client[Config.MONGO_DATABASE_NAME]
    return db


class Base():
    document_name = ''
