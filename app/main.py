from flask import Flask
from flask_login import LoginManager
from flask_pymongo import PyMongo
from config.config import Config


mongo = PyMongo()
login_manager = LoginManager()

app = Flask(__name__)
app.config.from_object(Config)

mongo.init_app(app)
login_manager.init_app(app)
