from flask import Blueprint, render_template

routes_bp = Blueprint('routes', __name__)


@routes_bp.route('/users')
def list_users():

    users = []
    return render_template('admin/users.html', users=users)
