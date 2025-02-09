import os
import base64

from werkzeug.utils import secure_filename

from app.config import config
from app.database import db


def get_avatar_base64(avatar_data):
    if avatar_data:
        return base64.b64encode(avatar_data).decode('utf-8')
    return None


def save_files(file, user):
    filename = secure_filename(file.filename)
    file_path = os.path.join(config.UPLOAD_FOLDER, filename)
    file.save(file_path)

    with open(file_path, 'rb') as image_file:
        avatar_data = image_file.read()
    user.avatar = get_avatar_base64(avatar_data)
    db.users.update_one({'user_id': user.user_id}, {'$set': {'avatar': user.avatar}})

    os.remove(file_path)


def get_profile_image():
    with open(config.AVATAR_PLACEHOLDER, 'r', encoding='utf-8') as f:
        avatar = f.read()
    return avatar


def get_page_image():
    with open(config.PLACEHOLDER, 'r', encoding='utf-8') as f:
        placeholder = f.read()
    return placeholder
