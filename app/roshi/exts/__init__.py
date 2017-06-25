"""
Roshi
~~~~~

Dynamic and (hopefully) replaceable pluggable extensions.

Note that the keys in EXTENSIONS will override the module name when
importing.  The following will import the global variable in this
module not the module in this package.:

    from roshi.exts import cache

To access a module in this package, use:

    from roshi.exts.cache import CACHE

Although, the modules in this package are not meant to be accessed
directly.  Import the needed functionality here to export:

    from .templating import render_template


:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

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
