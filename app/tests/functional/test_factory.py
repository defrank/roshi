"""
Application factory testing.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from flask import Flask  # type: ignore


def test_create_app(app):
    """Test creating application."""
    assert isinstance(app, Flask)


def test_blueprints(app):
    """Test correct blueprints installed in application."""
    blueprints = {'home'}
    assert blueprints == app.blueprints.keys()


def test_extensions(app):
    """Test correct extensions installed in application."""
    extensions = {'mako'}
    assert extensions == app.extensions.keys()
