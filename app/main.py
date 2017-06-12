from flask import Flask
from flask_mako import MakoTemplates


app = Flask(__name__)
mako = MakoTemplates(app)


@app.route('/')
def index():
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
