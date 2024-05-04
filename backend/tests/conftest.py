import os

import pytest

from backend import create_app, insert_data
from backend.extensions import db
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database(test_client):
    with test_client.application.app_context():
        db.create_all()
        insert_data()

    yield db # this is where the testing happens!

    db.drop_all()