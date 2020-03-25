import pytest
from api import create_app
from api import db as _db


@pytest.fixture
def app():
    app = create_app(config_name='testing')
    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            _db.drop_all()
            _db.create_all()
        yield client

@pytest.fixture
def db(app):
    """
    Creates an app context for the db and closes the session after execution is completed
    :param app:
    :return:
    """
    app.app_context().push()
    _db.init_app(app)
    _db.create_all()

    yield _db
    _db.session.close()
    _db.drop_all()
