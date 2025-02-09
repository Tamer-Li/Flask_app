from flask import Blueprint, render_template, session, request, redirect, url_for, flash

from app.utils.get_data import get_pages, get_users, get_my_pages, get_current_user
from app.utils.save_collections import save_pages, save_user
from app.utils.files_edit import save_files, get_profile_image

routes_bp = Blueprint('routes', __name__)


@routes_bp.route('/')
def pages():
    pages_list = get_pages()

    return render_template('pages/pages_view_list.html', pages=pages_list)


@routes_bp.route('/users')
def users():
    users_list = get_users()
    return render_template('pages/users.html', users=users_list)


@routes_bp.route('/mypages')
def my_pages():
    my_pages_list = get_my_pages(session.get('user_id'))
    return render_template('pages/my_pages.html', pages=my_pages_list)


@routes_bp.route('/create', methods=['GET', 'POST'])
def create_page():
    if request.method == 'POST':
        owner_id = int(session.get('user_id'))
        tag = request.form['tag']
        title = request.form['title']
        description = request.form.get('description', '')
        keywords = request.form.get('keywords', '')
        body = request.form.get('body', '')

        files = []
        if 'files' in request.files:
            for file in request.files.getlist('files'):
                files.append(file.read())

        if save_pages(
                owner_id,
                tag,
                title,
                description,
                keywords,
                body,
                files
        ):
            flash('Успешное сохранение страницы', 'success')
            return redirect(url_for('routes.pages'))

        flash('Не удалось сохранить страницу', 'danger')
        return render_template('pages/create_page.html')

    return render_template('pages/create_page.html')


@routes_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    user = get_current_user(int(session.get('user_id')))
    if not user:
        return redirect(url_for('auth.login'))

    avatar_base64: str
    if not user.avatar:
        avatar_base64 = get_profile_image()
    else:
        avatar_base64 = user.avatar

    if request.method == 'POST':
        form_type = request.form['form_type']

        if form_type == 'profile':
            user.user_name = request.form['user_name']
            user.email = request.form['email']

            if save_user(user):
                flash('Профиль успешно обновлен!', 'success')
                return redirect(url_for('routes.profile'))
            else:
                flash('Ошибка при обновлении данных профиля', 'danger')

        elif form_type == 'password':
            old_password = request.form.get('old_password')
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')

            if not user.check_password(old_password):
                flash('Неверный старый пароль.', 'danger')
            elif new_password != confirm_password:
                flash('Новый пароль и подтверждение не совпадают.', 'danger')
            else:
                user.set_password(new_password)

                if save_user(user):
                    flash('Пароль успешно изменен!', 'success')
                    return redirect(url_for('routes.profile'))
                else:
                    flash('Ошибка при обновлении данных профиля', 'danger')

        elif form_type == 'avatar':
            if 'avatar' in request.files:
                file = request.files['avatar']
                if file.filename != '':
                    if save_files(file, user):
                        flash('Аватарка успешно обновлена!', 'success')
                    else:
                        flash('Ошибка обновления', 'danger')
            else:
                flash('Необходимо выбрать файл.', 'danger')

        return redirect(url_for('routes.profile'))

    return render_template('pages/profile.html', user=user, avatar_base64=avatar_base64)

