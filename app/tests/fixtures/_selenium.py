"""
Selenium fixtures.

Inspired by:
    https://github.com/pallets/flask/blob/master/examples/flaskr/tests/test_flaskr.py

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from pytest import fixture  # type: ignore
from selenium import webdriver as _webdriver  # type: ignore


__all__ = [
    'webdriver',
]


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
