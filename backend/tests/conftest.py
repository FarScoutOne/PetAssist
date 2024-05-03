import os

import pytest
from backend import create_app
from backend.extensions import db
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    # app.config['TESTING'] = True
    # os.environ["FLASK_ENV"] = "testing"

    # Use SQLite for testing, you can replace it with other databases if needed
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'

    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database(test_client):
    with test_client.application.app_context():
        db.create_all()

    yield db # this is where the testing happens!

    db.drop_all()
