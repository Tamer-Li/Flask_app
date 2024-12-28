from datetime import datetime


class User:
    def __init__(
            self,
            user_id,
            user_name,
            password,
            email,
            is_active=True,
            signup_time=None,
            last_visit=None,
            account_type=3,
            avatar=None
    ):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.email = email
        self.is_active = is_active
        self.signup_time = signup_time or datetime.utcnow()
        self.last_visit = last_visit or datetime.utcnow()
        self.account_type = account_type
        self.avatar = avatar

    def check_password(self, password):
        return self.password, password

    def get_account_status(self):
        if not self.is_active and self.last_visit:
            return 4
        delta = (datetime.utcnow() - self.last_visit).days
        if delta < 8:
            return 1
        elif 7 < delta < 31:
            return 2
        else:
            return 3

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "user_name": self.user_name,
            "password": self.password,
            "email": self.email,
            "is_active": self.is_active,
            "signup_time": self.signup_time,
            "last_visit": self.last_visit,
            "account_type": self.account_type,
            "avatar": self.avatar
        }

    @staticmethod
    def from_dict(data):
        return User(
            user_id=data["user_id"],
            user_name=data["user_name"],
            password=data["password"],
            email=data["email"],
            is_active=data["is_active"],
            signup_time=data["signup_time"],
            last_visit=data["last_visit"],
            account_type=data.get("account_type", 3),
            avatar=data.get("avatar")
        )


class Page:
    def __init__(
            self,
            page_id,
            owner_id,
            tag,
            title,
            description=None,
            keywords=None,
            body=None,
            files=None
    ):
        self.page_id = page_id
        self.owner_id = owner_id
        self.tag = tag
        self.title = title
        self.description = description
        self.keywords = keywords
        self.body = body
        self.files = files or []

    def to_dict(self):
        return {
            "page_id": self.page_id,
            "owner_id": self.owner_id,
            "tag": self.tag,
            "title": self.title,
            "description": self.description,
            "keywords": self.keywords,
            "body": self.body,
            "files": self.files
        }

    @staticmethod
    def from_dict(data):
        return Page(
            page_id=data["page_id"],
            owner_id=data["owner_id"],
            tag=data["tag"],
            title=data["title"],
            description=data.get("description"),
            keywords=data.get("keywords"),
            body=data.get("body"),
            files=data.get("files", [])
        )


class Access:
    def __init__(self, acl_id, page_id, privilege, user_list):
        self.acl_id = acl_id
        self.page_id = page_id
        self.privilege = privilege
        self.user_list = user_list

    def to_dict(self):
        return {
            "acl_id": self.acl_id,
            "page_id": self.page_id,
            "privilege": self.privilege,
            "list": self.user_list
        }

    @staticmethod
    def from_dict(data):
        return Access(
            acl_id=data["acl_id"],
            page_id=data["page_id"],
            privilege=data["privilege"],
            user_list=data["list"]
        )
