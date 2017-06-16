"""
Run the `project` package as main.  This is a developement only way to
run this web app especially since it runs in debug mode.

    % python3 -m project


The preferred way to run is using Gunicorn and import the project's app.

    % gunicorn -b "0.0.0.0:5000" project:app


We hackily add the project directory to the python path so that we can
import from it as __main__.

"""
import sys
from os.path import dirname, join


PROJECT_PATH = join(dirname(sys.modules[__name__].__file__), '..')


if __name__ == '__main__':
    sys.path.insert(0, PROJECT_PATH)

    from project.app import run
    run(debug=True)
