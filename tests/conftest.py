import pytest

from wsgi.views import app as app_runner, engine_db


@pytest.fixture
def app():
    return app_runner


@pytest.fixture
def db():
    return engine_db
