"""
Base page object model.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from typing import Optional


class BasePage:
    # pylint: disable=too-few-public-methods
    """
    Abstract base page.  Tries to proxy to the given webdriver.

    """
    path: Optional[str] = None

    def __init__(self, webdriver, live_server):
        self.driver = webdriver
        self.live_server = live_server

        self.driver.get(self.live_server.url(self.path))

    def __getattr__(self, attr):
        """Proxy to webdriver."""
        return getattr(self.driver, attr)
