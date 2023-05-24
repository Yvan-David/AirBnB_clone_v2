#!/usr/bin/python3
""" Starting a flask web application
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """hello on the web """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """prints hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    """ c is text on the web """
    result = text.replace("_", " ")
    return f'C {result}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
