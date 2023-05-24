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
    result = text.replace("_", " ")
    return f'C {result}'


@app.route('/c', strict_slashes=False)
def hello_pytext():
    """prints hello on the web """
    return 'c is cool'


@app.route('/python', strict_slashes=False)
def hello_pytext():
    """prints hello on the web """
    return f'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def hello_pythtext(text):
    """prints hello on the web """
    result = text.replace("_", " ")
    return f'Python {result}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
