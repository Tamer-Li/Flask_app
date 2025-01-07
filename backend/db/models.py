from datetime import datetime


class User():
    document_name = 'users'

    def __init__(
            self,
            user_id: int,
            user_name: str,
            password: str,
            email: str,
            is_active: bool = True,
            signup_time: datetime = datetime.utcnow(),
            last_visit: datetime = datetime.utcnow(),
            account_type: int = 3,
            avatar: str = ""
    ):
        self._user_id = user_id
        self._user_name = user_name
        self._password = password
        self._email = email
        self._is_active = is_active
        self._signup_time = signup_time or datetime.utcnow()
        self._last_visit = last_visit or datetime.utcnow()
        self._account_type = account_type
        self._avatar = avatar

    def to_dict(self):
        return {
            "user_id": self._user_id,
            "user_name": self._user_name,
            "password": self._password,
            "email": self._email,
            "is_active": self._is_active,
            "signup_time": self._signup_time,
            "last_visit": self._last_visit,
            "account_type": self._account_type,
            "avatar": self._avatar
        }

    @staticmethod
    def from_dict(data):
        return User(
            user_id=data["user_id"],
            user_name=data["user_name"],
            password=data["password"],
            email=data["email"],
            is_active=data.get("is_active", True),
            signup_time=data.get("signup_time", datetime.utcnow()),
            last_visit=data.get("last_visit", datetime.utcnow()),
            account_type=data.get("account_type", 3),
            avatar=data.get("avatar", "")
        )

    @classmethod
    def get_account_status(self):
        if not self._is_active and self._last_visit:
            return 4
        delta = (datetime.utcnow() - self._last_visit).days
        if delta < 8:
            return 1
        elif 7 < delta < 31:
            return 2
        else:
            return 3


class Page():
    document_name = 'pages'

    def __init__(
            self,
            page_id: int,
            owner_id: int,
            tag: str,
            title: str,
            description: str = None,
            keywords: str = None,
            body: str = None,
            files: list[str] = None
    ):
        self._page_id = page_id
        self._owner_id = owner_id
        self._tag = tag
        self._title = title
        self._description = description
        self._keywords = keywords
        self._body = body
        self._files = files or []

    def to_dict(self):
        return {
            "page_id": self._page_id,
            "owner_id": self._owner_id,
            "tag": self._tag,
            "title": self._title,
            "description": self._description,
            "keywords": self._keywords,
            "body": self._body,
            "files": self._files
        }

    @staticmethod
    def from_dict(data):
        return Page(
            page_id=data["page_id"],
            owner_id=data["owner_id"],
            tag=data["tag"],
            title=data["title"],
            description=data.get("description", "Null"),
            keywords=data.get("keywords"),
            body=data.get("body"),
            files=data.get("files", [])
        )


class Access():
    document_name = 'access'

    def __init__(
            self,
            acl_id: int,
            page_id: int,
            privilege: str,
            user_list: list[int]
    ):
        self._acl_id = acl_id
        self._page_id = page_id
        self._privilege = privilege
        self._user_list = user_list

    def to_dict(self):
        return {
            "acl_id": self._acl_id,
            "page_id": self._page_id,
            "privilege": self._privilege,
            "list": self._user_list
        }

    @staticmethod
    def from_dict(data):
        return Access(
            acl_id=data["acl_id"],
            page_id=data["page_id"],
            privilege=data["privilege"],
            user_list=data["list"]
        )
