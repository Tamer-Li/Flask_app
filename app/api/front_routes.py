from flask import Blueprint, render_template, session, redirect, url_for
from app.models.collections.page import Page

front_bp = Blueprint('front', __name__)


@front_bp.route('/')
def index():
    pages = Page.objects.all()
    return render_template('index.html', pages=pages)


@front_bp.route('/page/<tag>')
def show_page(tag):
    page = Page.objects(tag=tag).first()
    if not page:
        return "Страница не найдена", 404

    return render_template('page.html', page=page)


@front_bp.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    return render_template('profile.html')
