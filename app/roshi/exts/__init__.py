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

from .cache import CACHE
from .csrf import CSRF
from .database import DB
from .login_manager import LOGIN_MANAGER
from .mail import MAIL
from .manager import MANAGER
from .migration import MIGRATE
from .pages import PAGES
from .testing import TESTING
from .task_queue import TQ
from .templating import TPL
from .translation import TRANSL


EXTENSIONS: Dict[str, Any] = {
    'cache': CACHE,
    'csrf':  CSRF,
    'db': DB,
    'login_manager': LOGIN_MANAGER,
    'mail': MAIL,
    'manager': MANAGER,
    'migrate': MIGRATE,
    'pages': PAGES,
    'testing': TESTING,
    'tq': TQ,
    'tpl': TPL,
    'transl': TRANSL,
}


# Add extensions to module-level.
globals().update(EXTENSIONS)
