from flask import request, flash, redirect, url_for, render_template

from flask import Blueprint

from app.utils.delete_data import delete_page_from_db
from app.utils.get_data import get_view_page

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
    if page:
        return render_template('pages/page.html', page=page)

    flash('Страница не найдена', 'danger')
    return redirect(url_for('routes'))
