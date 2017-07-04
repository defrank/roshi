"""
Page object model.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""


class BasePage:
    """
    Abstract base page.  Tries to proxy to the given webdriver.

    """

    def __init__(self, webdriver, url):
        self.url = url

        self.driver = webdriver
        self.driver.get(url)

    def __getattr__(self, attr):
        """Proxy to webdriver."""
        return getattr(self.driver, attr)


class HomePage(BasePage):
    """Homepage."""

    def __init__(self, *args, **kwargs):
        super(HomePage, self).__init__(*args, **kwargs)
