from flask import Flask
from flask_cors import CORS

from .extensions import db
from .routes import main, insert_data


def create_app():
    app = Flask(__name__)

    # Enable CORS
    CORS(app)

    app.config.from_prefixed_env()

    db.init_app(app)

    app.register_blueprint(main)
    return app
