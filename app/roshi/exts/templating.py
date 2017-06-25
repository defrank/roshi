"""
Roshi
~~~~~

Templating plugin.

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from typing import Optional

from flask_mako import MakoTemplates  # type: ignore


TPL: Optional[MakoTemplates] = MakoTemplates()
