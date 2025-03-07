import json

from pymongo import MongoClient

from app.config import config
from app.models.user import User

mongo = MongoClient(config.MONGO_HOST, config.MONGO_PORT)

db = mongo.archive

collections = db.list_collection_names()
required_collections = {'users', 'pages', 'access'}

if not required_collections.issubset(collections):
    print("Не все коллекции существуют. Создаем недостающие...")
    for coll in required_collections:
        if coll not in collections:
            db.create_collection(coll)
            print(f"Коллекция {coll} создана.")
else:
    print("Все коллекции существуют.")


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_test_json():
    users_data = load_json('app/data_test/users.json')
    pages_data = load_json('app/data_test/pages.json')
    access_data = load_json('app/data_test/access.json')

    if db.users.count_documents({}) == 0:
        for user in users_data:
            u = User(**user)
            u.set_password(user['password'])
            db.users.insert_one(u.to_dict())
        print("Коллекция users заполнена.")

    if db.pages.count_documents({}) == 0:
        db.pages.insert_many(pages_data)
        print("Коллекция pages заполнена.")

    if db.access.count_documents({}) == 0:
        db.access.insert_many(access_data)
        print("Коллекция access заполнена.")
