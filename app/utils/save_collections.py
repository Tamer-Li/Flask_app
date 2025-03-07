import logging
from typing import Optional, List

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

def update_page(
    page_id: int,
    tag: Optional[str] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    keywords: Optional[str] = None,
    body: Optional[str] = None,
    files: Optional[List[bytes]] = None
) -> bool:
    """
    Обновляет данные страницы в базе данных.

    :param page_id: Идентификатор страницы для обновления.
    :param tag: Новый тег страницы (опционально).
    :param title: Новый заголовок страницы (опционально).
    :param description: Новое описание страницы (опционально).
    :param keywords: Новые ключевые слова страницы (опционально).
    :param body: Новый текст страницы (опционально).
    :param files: Новые прикрепленные файлы (опционально).
    :return: True, если обновление прошло успешно, иначе False.
    """
    try:
        update_data = {}
        if tag is not None:
            update_data['tag'] = tag
        if title is not None:
            update_data['title'] = title
        if description is not None:
            update_data['description'] = description
        if keywords is not None:
            update_data['keywords'] = keywords
        if body is not None:
            update_data['body'] = body
        if files is not None:

            if len(files) == 0:
                files = None
            if len(files) == 1 and files[0] == b'':
                files = None
            update_data['files'] = files

        if update_data:
            db.pages.update_one(
                {'page_id': page_id},
                {'$set': update_data}
            )
            return True
        else:
            logging.warning("No data provided to update the page.")
            return False

    except Exception as e:
        logging.error(f"Failed to update page {page_id}: {e}")
        return False