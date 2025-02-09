import base64
from typing import List

from app.database import db
from app.models.user import User
from app.models.page import Page

from app.utils.files_edit import get_page_image, get_profile_image


def get_pages():
    pages = db.pages.find({})
    view_pages = []

    for page in pages:
        page_current = Page(**page)
        if not page_current.files:
            page_current.files = get_page_image()

        view_pages.append(page_current.to_dict())

    return view_pages


def get_users():
    users = list(db.users.find())
    view_users = []

    for user in users:
        user_current = User(**user)
        if user_current.avatar is None:
            user_current.avatar = get_profile_image()

        view_users.append(user_current.to_dict())

    return view_users


def get_current_user(user_id):
    user_data = db.users.find_one({'user_id': user_id})
    if user_data:
        return User(**user_data)
    return None


def get_my_pages(user_id: int):
    pages = list(db.pages.find({"owner_id": int(user_id)}))
    view_pages = []

    for page in pages:
        page_current = Page(**page)
        if not page_current.files:
            page_current.files = get_page_image()

        view_pages.append(page_current.to_dict())

    return view_pages


def get_avatar_base64(avatar_data):
    if avatar_data:
        return base64.b64encode(avatar_data).decode('utf-8')
    return None
