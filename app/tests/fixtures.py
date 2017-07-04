# pylint: disable=redefined-outer-name,unused-argument
"""
Testing fixtures.

Inspired by:
    https://github.com/pallets/flask/blob/master/examples/flaskr/tests/test_flaskr.py

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from pytest import fixture  # type: ignore
from selenium import webdriver as _webdriver  # type: ignore

from roshi.factory import create_app
from .models.page import HomePage


@fixture
def app(request):
    """Roshi create application fixture."""
    _app = create_app()

    with _app.app_context():
        yield _app


@fixture
def config(app):
    """The application config."""
    return app.config


@fixture(params=['Chrome', 'Firefox'])
def webdriver(request):
    """
    Chrome Selenium webdriver.

    Requirements:

        Chrome - chromedriver
        Firefox - geckodriver

    Install (macOS):

        brew install chromedriver geckodriver

    """
    driver = getattr(_webdriver, request.param)()
    yield driver
    driver.quit()


@fixture
def page(live_server, webdriver):
    """Home page object."""
    yield HomePage(webdriver, live_server.url('/'))
