from flask import request, flash, redirect, url_for, render_template, session

from flask import Blueprint

from app.utils.delete_data import delete_page_from_db
from app.utils.get_data import get_view_page, is_admin_user, get_access
from app.utils.save_collections import update_page


page_routes = Blueprint('page_routes', __name__)


@page_routes.route('/delete/<int:page_id>', methods=['POST'])
def delete_page(page_id: int):
    if request.method == 'POST':
        if delete_page_from_db(page_id=page_id):
            flash('Страница успешно удалена', 'success')
        flash('Ошибка при удалении страницы', 'danger')
        return redirect(url_for('routes'))
    return redirect(url_for('routes'))


@page_routes.route('/<int:page_id>', methods=['GET'])
def view_page(page_id: int):
    page = get_view_page(page_id)
    admin = False
    user_id = int(session['user_id'])

    if is_admin_user(user_id):
        admin = True

    if page:
        return render_template('pages/page.html', page=page, admin=admin)

    flash('Страница не найдена', 'danger')
    return redirect(url_for('routes'))

@page_routes.route('/change/<int:page_id>', methods=['GET', 'POST'])
def change_page(page_id: int):
    if request.method == 'POST':

        page_id = request.form['page_id']
        tag = request.form['tag']
        title = request.form['title']
        description = request.form['description']
        keywords = request.form.get('keywords', '')
        body = request.form['body']
        files = []
        if 'files' in request.files:
            for file in request.files.getlist('files'):
                files.append(file.read())
        if update_page(
                page_id,
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

    access = get_access(page_id)
    if access != 'none':
        access = []
    
    page = get_view_page(page_id)

    return render_template('pages/edit_page.html', page=page, access=access)
