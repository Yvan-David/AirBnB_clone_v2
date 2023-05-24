#!/usr/bin/python3
""" Starting a flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prints hello on the web """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """prints hello on the web """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    """prints hello on the web """
    return f'C is {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
