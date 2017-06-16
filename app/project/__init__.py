from flask import Flask
from flask_mako import MakoTemplates

from .views.home import home


app = Flask(__name__)
mako = MakoTemplates(app)
app.register_blueprint(home)
