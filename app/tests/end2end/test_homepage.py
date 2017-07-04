"""
Test the homepage.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""


# Sally hears about a new dog training webapp.
# She goes to the homepage.
def test_basic(page):
    """Basic testing."""
    assert page.title == ''
    assert 'Welcome home!' in page.page_source
