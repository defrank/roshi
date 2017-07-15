# pylint: disable=redefined-outer-name
"""
Test name utility.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from pytest import fixture

from roshi.utils.name import Name


SHORT = 'example'
LONG = 'Long Example'


@fixture
def name():
    """Fixture to instantiate common Name instance."""
    return Name(SHORT, LONG)


class NameTests:
    """Class Name tests."""

    @staticmethod
    def test_basic_args_given(name):
        """Verify input exists in output."""
        assert name.default == SHORT
        assert name.long == LONG

    @staticmethod
    def test_str_method(name):
        """Verify default represents `str(name)`."""
        assert str(name) == SHORT
        assert str(name) == str(name.default)
        assert str(name.default) == SHORT
        assert str(name.long) == LONG

    @staticmethod
    def test_default_proxy(name):
        """Verify default attribute gets called for missing methods."""
        assert name.lower() == SHORT.lower()
        assert name.upper() == SHORT.upper()
        assert name.title() == SHORT.title()
        assert name.capitalize() == SHORT.capitalize()

        assert name.lower() != LONG.lower()
        assert name.upper() != LONG.upper()
        assert name.title() != LONG.title()
        assert name.capitalize() != LONG.capitalize()
