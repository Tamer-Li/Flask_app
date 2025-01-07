from flask import Flask, jsonify
from flask_cors import CORS

from backend.settings.config import config
from backend.api.auth import auth_br


app = Flask(__name__)

app.config.from_object(config)

CORS(app)


@app.route('/api_v1', methods=['GET'])
def root():
    return jsonify({
        "Hello": "World"
    })


app.register_blueprint(auth_br)

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
