from flask import Blueprint, render_template, redirect, url_for, flash, session, request

from app.models.user import User
from app.database import db

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('Заполните все поля', 'danger')
            return render_template('auth/login.html')

        user_data = db.users.find_one({'email': email})
        if user_data:
            user = User(**user_data)
            if user.check_password(password):
                session['user_id'] = str(user.user_id)
                session['account_type'] = user.account_type

                flash('Вы успешно вошли в систему!', 'success')
                return redirect(url_for('routes.pages'))
            else:
                flash('Неверный пароль', 'danger')
        else:
            flash('Пользователь не найден', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        if not email or not username or not password:
            flash('Заполните все поля', 'danger')
            return render_template('auth/register.html')

        user_data = db.users.find_one({'email': email})

        if user_data:
            flash('Такой email уже зарегистрирован', 'danger')
            return redirect(url_for('auth/register.html'))

        user_id = db.users.count_documents({})
        new_user = User(
            user_id=user_id+1,
            user_name=username,
            password=password,
            email=email,
        )
        new_user.set_password(password=password)
        db.users.insert_one(new_user.to_dict())

        flash('Вы успешно зарегистрированы!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('account_type', None)
    flash('Вы вышли из системы', 'info')
    return redirect(url_for('index'))
