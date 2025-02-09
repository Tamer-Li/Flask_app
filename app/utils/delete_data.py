from app.database import db


def delete_page_from_db(page_id: int) -> bool:
    try:
        db.pages.delete_one({'page_id': page_id})
        return True

    except Exception as e:
        return False
