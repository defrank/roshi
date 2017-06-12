from flask import Blueprint


home = Blueprint('home', __name__)


@home.route('/')
def index() -> str:
    return 'Hello, world!'


@home.route('/<id_>')
def test_arg(id_: int) -> str:
    return 'id is {}'.format(id_)



