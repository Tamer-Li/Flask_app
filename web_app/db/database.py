from pymongo import MongoClient

from web_app.settings.config import config


def get_db_connection():
    client = MongoClient(config.MONGO_URL)
    db = client[config.MONGO_DATABASE_NAME]
    return db


class Base:
    document_name = ''
