import os
from dotenv import load_dotenv


load_dotenv('../.env')


class Config:
    MONGO_URL = os.getenv('MONGO_URL')
    MONGO_DATABASE_NAME = os.getenv('MONGO_DATABASE_NAME')
    SECRET_KEY = os.getenv('SECRET_KEY')
    HASH_ALGORITHM = os.getenv('HASH_ALGORITHM')


config = Config()
print(config)
