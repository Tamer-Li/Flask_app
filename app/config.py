import os
from dotenv import load_dotenv


load_dotenv('../.env')
secret_key = os.urandom(24).hex()


class BaseConfig:
    MONGO_HOST: str = os.getenv('MONGO_HOST', 'mongodb')
    MONGO_PORT: int = int(os.getenv('MONGO_PORT', '27017'))
    MONGO_DATABASE_NAME: str = os.getenv('MONGO_DATABASE_NAME', 'archive')
    SECRET_KEY: str = os.getenv('SECRET_KEY', secret_key)
    HASH_ALGORITHM: str = os.getenv('HASH_ALGORITHM', 'sha256')
    HOST: str = os.getenv('HOST', '0.0.0.0')
    PORT: int = int(os.getenv('PORT', '5000'))
    ADMIN_NAME: str = os.getenv('ADMIN_NAME', 'admin')
    ADMIN_PASSWORD: str = os.getenv('ADMIN_PASSWORD', 'admin')
    ADMIN_EMAIL: str = os.getenv('ADMIN_EMAIL', 'admin@mail.ru')
    DEBUG: bool = True
    UPLOAD_FOLDER: str = os.getenv('UPLOAD_FOLDER', 'static/avatars')
    AVATAR_PLACEHOLDER: str = os.getenv('AVATAR_PLACEHOLDER', 'static/avatars/avatar.txt')
    PLACEHOLDER: str = os.getenv('PLACEHOLDER', 'static/images/placeholder.txt')


config = BaseConfig()
