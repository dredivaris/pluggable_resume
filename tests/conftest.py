import pytest

from wsgi.setup import app as app_runner, engine_db

MONGODB_HOST = 'localhost'
SESSION_TYPE = 'mongodb'
SECRET_KEY = 'jkJKJGFDKJ*hG*&YD)JPSDGJLSKDJGOISUojidlsfkjasgd08adgpijG(HD('
MONGODB_DB = 'andreas_website_test'
MONGO_DBNAME = 'andreaswebsitetest'


@pytest.fixture
def app(scope='session'):
    return app_runner


@pytest.fixture
def real_db():
    return engine_db


@pytest.fixture(scope='session')
def db(app, request):
    pass
    # def teardown():
    #     _db.drop_all()
    #     os.unlink(TESTDB_PATH)
    #
    # _db.app = app
    # _db.create_all()
    #
    # request.addfinalizer(teardown)
    # return _db
