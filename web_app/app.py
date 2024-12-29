from flask import Flask, render_template

from web_app.settings.config import config
from web_app.auth.auth_route import auth_bp


app = Flask(
    __name__,
    template_folder='./templates',
    static_folder='./static',
)
app.config.from_object(config)


@app.route('/')
def index():
    return render_template('base.html')


app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
