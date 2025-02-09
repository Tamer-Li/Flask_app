import logging
from typing import Optional, List
import datetime

from app.database import db
from app.models.page import Page
from app.models.user import User


def save_pages(
    owner_id: int,
    tag: str,
    title: str,
    description: Optional[str] = None,
    keywords: Optional[str] = None,
    body: Optional[str] = None,
    files: Optional[List[bytes]] = None
):
    try:
        if len(files) == 0:
            files = None

        if len(files) == 1 and files[0] == b'':
            files = None

        page_id = int(db.pages.count_documents({}))
        new_page = Page(
            page_id=page_id,
            owner_id=owner_id,
            tag=tag,
            title=title,
            description=description,
            keywords=keywords,
            body=body,
            files=files
        )
        db.pages.insert_one(new_page.to_dict())

        return True

    except Exception as e:
        logging.error(f"Failed to save page: {e}")
        return False


def save_user(user: User):

    try:
        db.users.update_one(
            {'user_id': user.user_id},
            {'$set': user.to_dict()}
        )

        return True

    except Exception as e:
        logging.error(f"Failed to save user: {e}")
        return False
