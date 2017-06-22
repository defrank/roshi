"""
Templating plugin.

"""
from typing import Optional

from flask_mako import MakoTemplates  # type: ignore


tpl: Optional[MakoTemplates] = MakoTemplates()
