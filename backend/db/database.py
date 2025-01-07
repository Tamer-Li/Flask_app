from pymongo import MongoClient

from backend.settings.config import config


def get_db_connection():
    client = MongoClient(config.MONGO_URL)
    db = client[config.MONGO_DATABASE_NAME]
    return db
