import pytest

from flaskr import create_app


@pytest.fixture
def app():
    # db_fd, db_path = tempfile.mkstemp()

    app = create_app(test_config=True)

    yield app

    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
