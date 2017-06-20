from flask import Blueprint  # type: ignore
from flask_mako import render_template  # type: ignore


home = Blueprint('home', __name__)  # type: Blueprint


@home.route('/')
def index() -> str:
    return render_template('home/index.mako', message='Welcome home!')
