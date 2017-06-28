"""
Testing fixtures.

Inspired by:
    https://github.com/pallets/flask/blob/master/examples/flaskr/tests/test_flaskr.py

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from pytest import fixture  # type: ignore

from roshi.factory import create_app


@fixture
def app(request):
    # pylint: disable=unused-argument
    """
    Roshi create application fixture.

    """
    application = create_app()

    with application.app_context():
        yield application


@fixture
def client(request, app):
    # pylint: disable=redefined-outer-name
    """
    Roshi create application client fixture.

    """
    client = app.test_client()

    def teardown():
        """Client teardown despite exceptions."""
        pass
    request.addfinalizer(teardown)

    return client
