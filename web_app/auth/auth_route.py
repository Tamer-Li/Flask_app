from datetime import datetime

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from web_app.auth.forms import LoginForm, RegistrationForm
from web_app.db.dao import UserDAO
from web_app.db.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_data = UserDAO.find_user_by_name(form.user_name.data)
        if user_data and check_password_hash(
            user_data['password'],
            form.password.data
        ):
            user_data["is_active"] = True
            user = User(**user_data)
            login_user(user)
            return redirect(url_for('api.index'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user_data = {
            'user_id': UserDAO.get_count_users() + 1,
            'user_name': form.user_name.data,
            'email': form.email.data,
            'password': generate_password_hash(form.password.data),
            'account_status': 1,
            'account_type': 3,
            'is_active': True,
            'signup_time': datetime.utcnow(),
            'last_visit': datetime.utcnow(),
            'avatar': ""
        }
        UserDAO.insert_user(User(**user_data))
        flash('Registration successful!')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('api.index'))
