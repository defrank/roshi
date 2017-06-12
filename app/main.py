from flask import Flask
from flask_mako import MakoTemplates

from views.home import home


app = Flask(__name__)
mako = MakoTemplates(app)
app.register_blueprint(home)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
