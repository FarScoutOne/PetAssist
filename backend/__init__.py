import os

from flask import Flask

from .extensions import db
from .routes import main, insert_data


def set_database_uri(app):
    env = os.getenv("FLASK_ENV", "production")
    print("**** ENVIRONMENT : ", env)
    database_uri = 'SQLALCHEMY_TEST_DATABASE_URI' if env == "testing" else 'SQLALCHEMY_DATABASE_URI'
    print("**** DATABASE_URI: ", database_uri)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(database_uri, 'sqlite:///fallback.sqlite')
    print("URI: ", os.getenv(database_uri))


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    set_database_uri(app)
    db.init_app(app)
    return app
