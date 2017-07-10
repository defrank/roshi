"""
Test fixtures.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from flask import Flask  # type: ignore


def test_simple_app(app):
    """Verify basic application."""
    assert isinstance(app, Flask)


def test_simple_config(config):
    """Verify basic application configuration."""
    assert isinstance(config, dict)


def test_webdriver_current_url(webdriver):
    """
    Verify data URL.

    Chrome: 'data:,'
    Firefox: 'about:blank'

    """
    assert webdriver.name in ['chrome', 'firefox']
    assert webdriver.current_url in ['data:,', 'about:blank']


def test_webdriver_get_google(webdriver):
    """If google is down, something bad has happened."""
    webdriver.get('http://google.com/')
    assert 'Google' in webdriver.title


def test_page_proxies_webdriver(homepage):
    """Verify webdriver proxying."""
    assert homepage.title == homepage.driver.title
    assert homepage.current_url == homepage.driver.current_url
    assert homepage.get == homepage.driver.get
