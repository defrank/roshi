"""
Dynamic and (hopefully) replaceable pluggable extensions.

"""
from flask_mako import MakoTemplates


EXTENSIONS = {
    'cache': None,
    'csrf':  None,
    'db': None,  # Database.
    'login_manager': None,
    'mail': None,
    'manager': None,
    'migrate': None,
    'pages': None,
    'testing': None,
    'tq': None,  # Task queue.
    'tpl': MakoTemplates(),  # Templating.
    'transl': None,  # Translation: i18n and l10n
}


# Add extensions to module-level.
globals().update(EXTENSIONS)
