from datetime import datetime

from app.db.models import User, Page, Access
from app.db.db import get_db_connection


class UserDAO:
    def __init__(self):
        self.db = get_db_connection()
        self.collection = self.db["users"]

    def insert_user(self, user: User):
        user_dict = user.to_dict()
        result = self.collection.insert_one(user_dict)
        return result.inserted_id

    def find_user_by_name(self, name: str):
        user_data = self.collection.find_one({"name": name})
        if user_data:
            return User.from_dict(user_data)
        return None

    def find_users_by_id(self, id: int):
        users = self.collection.find({"user_id": id})
        return [User.from_dict(user) for user in users]

    def update_user_email(self, user_id: int, new_email: str):
        result = self.collection.update_one(
            {"user_id": user_id},
            {"$set": {"email": new_email}}
        )
        return result.modified_count > 0

    def delete_user_by_name(self, name):
        result = self.collection.delete_one({"name": name})
        return result.deleted_count > 0

    def update_user_password(self, user_id: int, password: str):
        result = self.collection.update_one(
            {"user_id": user_id},
            {"$set": {"password", password}}
        )
        return result.modified_count > 0

    def update_user_name(self, user_id: int, name: str):
        result = self.collection.update_one(
            {"user_id": user_id},
            {"$set": {"name": name}}
        )
        return result.modified_count > 0

    def update_account_type(self, user_id: int, account_type: int):
        result = self.collection.update_one(
            {"user_id": user_id},
            {"$set": {"account_type": account_type}}
        )
        return result.modified_count > 0

    def update_is_active(self, user_id: int, is_active: bool):
        result = self.collection.update_one(
            {"user_id": user_id},
            {"$set": {"is_active": is_active}}
        )
        return result.modified_count > 0

    def update_last_visit(self, user_id: int, last_visit: datetime):
        result = self.collection.update_one(
            {"user_id": user_id},
            {"$set": {"last_visit": last_visit}}
        )
        return result.modified_count > 0

    def update_avatar(self, user_id: int, avatar: str):
        result = self.collection.update_one(
            {"user_id": user_id},
            {"$set": {"avatar": avatar}}
        )
        return result.modified_count > 0

    def get_count_users(self):
        results = self.collection.find()
        return len(results)


class PageDao:
    def __init__(self):
        self.db = get_db_connection()
        self.collection = self.db["pages"]

    def insert_page(self, page: Page):
        page_dict = page.to_dict()
        result = self.collection.insert_one(page_dict)
        return result.inserted_id

    def find_page_by_id(self, id: int):
        page_data = self.collection.find_one({"page_id": id})
        if page_data:
            return Page.from_dict(page_data)
        return None

    def find_page_by_owner(self, owner_id: int):
        pages_data = self.collection.find_one({"owner_id": owner_id})
        if pages_data:
            return [Page.from_dict(page) for page in pages_data]
        return None

    def find_page_all(self):
        pages = self.collection.find()
        return [Page.from_dict(page) for page in pages]

    def update_page_by_id_tag(self, page_id: int, tag: str):
        result = self.collection.update_one(
            {"page_id": page_id},
            {"$set": {"tag": tag}}
        )
        return result.modified_count > 0

    def delete_page_by_id(self, page_id: int):
        result = self.collection.delete_one({"page_id": page_id})
        return result.deleted_count > 0

    def update_page_title(self, page_id: int, title: str):
        result = self.collection.update_one(
            {"page_id": page_id},
            {"$set": {"title", title}}
        )
        return result.modified_count > 0

    def update_page_description(self, page_id: int, description: str):
        result = self.collection.update_one(
            {"page_id": page_id},
            {"$set": {"description": description}}
        )
        return result.modified_count > 0

    def update_page_keywords(self, page_id: int, keywords: str):
        result = self.collection.update_one(
            {"page_id": page_id},
            {"$set": {"keywords": keywords}}
        )
        return result.modified_count > 0

    def update_page_body(self, page_id: int, body: str):
        result = self.collection.update_one(
            {"page_id": page_id},
            {"$set": {"body": body}}
        )
        return result.modified_count > 0

    def update_page_files(self, page_id: int, files: list[str]):
        result = self.collection.update_one(
            {"page_id": page_id},
            {"$set": {"files": files}}
        )
        return result.modified_count > 0

    def get_count_pages(self):
        results = self.collection.find()
        return len(results)


class AccessDao:
    def __init__(self):
        self.db = get_db_connection()
        self.collection = self.db["access"]

    def insert_access(self, access: Access):
        access_dict = access.to_dict()
        result = self.collection.insert_one(access_dict)
        return result.inserted_id

    def find_access_by_id(self, id: int):
        access_data = self.collection.find_one({"access_id": id})
        if access_data:
            return Access.from_dict(access_data)
        return None

    def find_access_by_page(self, page_id: int):
        access_data = self.collection.find_one({"page_id": page_id})
        if access_data:
            return [Access.from_dict(access) for access in access_data]
        return None

    def update_access_privelege(self, acl_id: int, privilege: str):
        result = self.collection.update_one(
            {"acl_id": acl_id},
            {"$set": {"privilege": privilege}}
        )
        return result.modified_count > 0

    def delete_access_by_id(self, acl_id: int):
        result = self.collection.delete_one({"acl_id": acl_id})
        return result.deleted_count > 0

    def update_access_list(self, acl_id: int, access_list: list[int]):
        result = self.collection.update_one(
            {"acl_id": acl_id},
            {"$set": {"list", access_list}}
        )
        return result.modified_count > 0

    def get_count_access(self):
        results = self.collection.find()
        return len(results)
