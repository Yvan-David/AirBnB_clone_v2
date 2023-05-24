#!/usr/bin/python3
"""
Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    prints hello on the web.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    prints hello on the web.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def tet(text):
    """
    prints hello on the web.
    """
    result = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/c", strict_slashes=False)
def hello_pytext():
    """
    prints hello on the web.
    """
    return "c is cool"


@app.route("/python", strict_slashes=False)
def hello_pytext():
    """
    prints hello on the web.
    """
    return "Python is cool."


@app.route("/python/<text>", strict_slashes=False)
def hello_pythtext(text):
    """
    prints hello on the web.
    """
    result = text.replace("_", " ")
    return "Python {}".format(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
