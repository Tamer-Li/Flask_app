from flask import Flask, render_template

from config import config
from app.api.routes import routes_bp
from app.api.auth_routes import auth_bp
from app.api.page_routes import page_routes


app = Flask(__name__, static_folder='static', template_folder='templates')

app.config['MONGODB_SETTINGS'] = {
    'host': config.MONGO_HOST,
    'port': config.MONGO_PORT,
    'models': config.MONGO_DATABASE_NAME
}
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['UPLOAD_FOLDER'] = config.UPLOAD_FOLDER

app.register_blueprint(routes_bp, url_prefix='/elarch')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(page_routes, url_prefix='/page')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
