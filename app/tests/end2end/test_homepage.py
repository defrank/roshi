"""
Test the homepage.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""


# Sally hears about a new dog training webapp.
# She goes to the homepage.
def test_basic(homepage):
    """Basic testing."""
    assert homepage.title == ''


# She finds out a little more about the app.
def test_content_keywords(homepage):
    """Useful information on the homepage."""
    assert 'dog' in homepage.page_source
    assert 'training' in homepage.page_source
