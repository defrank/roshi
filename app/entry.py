"""
Entrypoint into the project.  Creates an exportable app for use with
WSGI servers like Gunicorn.

    % gunicorn -b "0.0.0.0:5000" entry:app

:copyright: (c) 2017 Derek M. Frank
:license: MPL-2.0

"""
from roshi.factory import create_app


app = create_app()


if __name__ == '__main__':
    from roshi.factory import run
    run(app, debug=False)
