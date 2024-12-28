from app.main import mongo


def get_user_by_username(username):
    return mongo.db.users.find_one({'username': username})


def insert_user(user_data):
    mongo.db.users.insert_one(user_data)


def get_all_users():
    return mongo.db.users.find()


def get_page_by_id(page_id):
    return mongo.db.pages.find_one({'_id': page_id})


def get_all_pages():
    return mongo.db.pages.find()


def insert_page(page_data):
    mongo.db.pages.insert_one(page_data)


def update_page(page_id, update_data):
    mongo.db.pages.update_one({'_id': page_id}, {'$set': update_data})


def delete_page(page_id):
    mongo.db.pages.delete_one({'_id': page_id})
