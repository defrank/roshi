"""
Roshi
~~~~~

Configure this application in Python.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from .utils.name import Name


NAME = Name('petiquette', 'Petiquette Dog Training App')

ALLOWED_DOMAINS = [
    'petiquette.dog',
    'petiquette.training',
    'petiquette.us',
    'petiquette.dev',
    'petiquette.local',
]
