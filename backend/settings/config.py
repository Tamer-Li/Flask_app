import os
from dotenv import load_dotenv


load_dotenv('../.env')


class Config:
    MONGO_URL = os.getenv('MONGO_URL')
    MONGO_DATABASE_NAME = os.getenv('MONGO_DATABASE_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY')
    HASH_ALGORITHM = os.getenv('HASH_ALGORITHM')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')
    ADMIN_NAME = os.getenv('ADMIN_NAME')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')


config = Config()
