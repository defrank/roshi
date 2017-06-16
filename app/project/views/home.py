from flask import Blueprint
from flask_mako import render_template


home = Blueprint('home', __name__)


@home.route('/')
def index() -> str:
    return render_template('home/index.mako', message='Welcome home!')