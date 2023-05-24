#!/usr/bin/python3
""" Starting a flask web application """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prints hello on the web """
    return 'Hello HBNB!'
