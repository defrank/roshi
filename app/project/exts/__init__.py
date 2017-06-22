"""
Dynamic and (hopefully) replaceable pluggable extensions.

"""
from typing import Any, Dict

from .cache import cache
from .csrf import csrf
from .database import db
from .login_manager import login_manager
from .mail import mail
from .manager import manager
from .migration import migrate
from .pages import pages
from .testing import testing
from .task_queue import tq
from .templating import tpl
from .translation import transl


EXTENSIONS: Dict[str, Any] = {
    'cache': cache,
    'csrf':  csrf,
    'db': db,
    'login_manager': login_manager,
    'mail': mail,
    'manager': manager,
    'migrate': migrate,
    'pages': pages,
    'testing': testing,
    'tq': tq,
    'tpl': tpl,
    'transl': transl,
}
