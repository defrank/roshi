"""
Roshi
~~~~~

Name utilities.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from collections import namedtuple


class Name(namedtuple('Name', ['default', 'long'])):
    """
    Name class to support a default (short) and long version of a name,
    as well as common str methods like lower and capitalize.

    """
    def __str__(self):
        return str(self.default)

    def __getattr__(self, attr):
        return getattr(self.default, attr)
