"""
Page object fixtures.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from pytest import fixture  # type: ignore

from ..models.home import HomePage


__all__ = [
    'homepage',
]


@fixture
def homepage(webdriver, live_server):
    """Home page object."""
    yield HomePage(webdriver, live_server)
