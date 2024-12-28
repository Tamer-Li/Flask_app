from flask import Flask, render_template
from flask_login import LoginManager

from web_app.config.config import Config

login_manager = LoginManager()

app = Flask(__name__, template_folder='./templates')
app.config.from_object(Config)

login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('base.html')
