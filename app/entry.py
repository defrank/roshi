"""
Entrypoint into the project.  Creates an exportable app for use with
WSGI servers like Gunicorn.

    % gunicorn -b "0.0.0.0:5000" entry:app

"""
from project import create_app


app = create_app()


if __name__ == '__main__':
    from project.factory import run
    run(app, debug=False)
