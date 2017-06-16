"""
Application structure is defined here.

Inspired by:
    https://github.com/xen/flask-project-template/blob/master/project/app.py

"""
from flask import Flask

from .extensions import EXTENSIONS
from .views.home import home


__all__ = [
    'create_app',
]

BLUEPRINTS = [
    home,
]


def run(app=None, *, debug=False):
    """Development-only version to run the app."""
    if app is None:
        app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=debug)


def create_app(config=None, app_name='project', blueprints=None):
    """Return the built and configured app."""

    app = Flask(app_name, template_folder='templates')

    app.config.from_object('project.config')
    app.config.from_pyfile('../secrets.cfg', silent=True)
    if config:
        app.config.from_pyfile(config)

    if blueprints is None:
        blueprints = BLUEPRINTS

    blueprints_fabrics(app, blueprints)
    extensions_fabrics(app)

    return app


def blueprints_fabrics(app, blueprints):
    """Configure blueprints in views."""

    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def extensions_fabrics(app):
    """Initialize the extensions with the given app."""
    for ext in EXTENSIONS.values():
        if ext:
            ext.init_app(app)
