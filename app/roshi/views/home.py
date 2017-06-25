"""
Roshi
~~~~~

Home views.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from flask import Blueprint  # type: ignore
from flask_mako import render_template  # type: ignore


home = Blueprint('home', __name__)  # type: Blueprint


@home.route('/')
def index() -> str:
    """
    The most important view.  Currently doesn't do anything :(

    """
    return render_template('home/index.mako', message='Welcome home!')
