from pymongo import MongoClient

from app.config import config

mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT)

db = mongo.archive
