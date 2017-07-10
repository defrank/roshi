"""
Testing fixtures.

Inspired by:
    https://github.com/pallets/flask/blob/master/examples/flaskr/tests/test_flaskr.py

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from pytest import fixture  # type: ignore

from roshi.factory import create_app


__all__ = [
    'app',
    'config',
]


@fixture
def app():
    """Roshi create application fixture."""
    _app = create_app()

    with _app.app_context():
        yield _app


@fixture
def config(app):
    # pylint: disable=redefined-outer-name
    """The application config."""
    return app.config
