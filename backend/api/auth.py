from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash

from backend.db.dao import UserDAO, User
from backend.settings.config import config

auth_br = Blueprint('auth', __name__)


@auth_br.route('/api_v1/login', methods=['GET', 'POST'])
def login(
    email: str,
    password_check: str
):
    try:
        u = UserDAO()
        user = u.find_user_by_email(email)
        if user is None:
            return jsonify({
                "error": "Not found"
            }), 400

        if user.get_account_status == 4:
            return jsonify({
                "error": "Block"
            }), 400

        user_data = user.to_dict()
        if check_password_hash(user_data['password'] == password_check):
            return jsonify(user_data), 201

        return jsonify({
            "error": "Fail"
        }), 400

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@auth_br.route('/api_v1/register', methods=['POST'])
def register():
    try:
        u = UserDAO()
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Необходимо указать данные"
            }), 400

        if 'user_name' not in data:
            return jsonify({
                "error": "Необходимо указать user_name"
            }), 400

        if 'email' not in data:
            return jsonify({
                "error": "Необходимо указать email"
            }), 400

        if 'password' not in data:
            return jsonify({
                "error": "Необходимо указать password"
            }), 400

        if u.find_user_by_email(data['email']) is not None:
            return jsonify({
                "error": "Пользователь с таким email уже существует"
            }), 400

        if u.find_user_by_name(data['user_name']) is not None:
            return jsonify({
                "error": "Пользователь с таким user_name уже существует"
            }), 400

        data['password'] = generate_password_hash(data['password'])
        new_user = User(
            user_id=u.get_count_users()+1,
            user_name=data.get('user_name', 'test'),
            password=data.get(
                'password',
                generate_password_hash('test')
            ),
            email=data.get('email', 'test@mail.ru'),
            is_active=True,
            signup_time=None,
            last_visit=None,
            account_type=3,
            avatar=None
        )
        result = u.insert_user(new_user)

        return jsonify({result}), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@auth_br.route('/api_v1/users', methods=['GET'])
def get_users():
    try:
        d = UserDAO()
        count = d.get_count_users()
        print(count)
        return jsonify({
            "COUNT": count
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@auth_br.route('/api_v1/test', methods=['GET'])
def get_test():
    try:
        d = UserDAO()
        result = d.find_users_by_id(1)
        return jsonify({
            "COUNT": [r.to_dict() for r in result]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@auth_br.route('/admin', methods=['POST'])
def admin_reg():
    try:
        u = UserDAO()
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "Необходимо указать данные"
            }), 400

        if 'user_name' not in data:
            return jsonify({
                "error": "Необходимо указать user_name"
            }), 400

        if 'email' not in data:
            return jsonify({
                "error": "Необходимо указать email"
            }), 400

        if 'password' not in data or data['password'] is None:
            return jsonify({
                "error": "Необходимо указать password"
            }), 400

        if u.find_user_by_email(data['email']) is not None:
            return jsonify({
                "error": "Пользователь с таким email уже существует"
            }), 400

        if u.find_user_by_name(data['user_name']) is not None:
            return jsonify({
                "error": "Пользователь с таким user_name уже существует"
            }), 400

        data['password'] = generate_password_hash(data.get(
                'password',
                generate_password_hash(str(config.ADMIN_PASSWORD))
            ))
        new_user = User(
            user_id=int(u.get_count_users())+1,
            user_name=data.get('user_name', str(config.ADMIN_NAME)),
            password=data['password'],
            email=data.get('email', str(config.ADMIN_EMAIL)),
            account_type=1,
        )
        u.insert_user(new_user)
        return jsonify({"result": "Success"}), 201

    except Exception as e:
        return jsonify({
            "error": str(e),
            "data": request.get_json()
        }), 500
