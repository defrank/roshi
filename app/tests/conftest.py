"""
Pytest implicit configuration.

We define fixtures in a separate module and import here for readability.
Importing fixtures here (root configuration) is important to be able to
have them accessible throughout the pacakge.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""


pytest_plugins = [  # pylint: disable=invalid-name
    'tests.fixtures',
]
