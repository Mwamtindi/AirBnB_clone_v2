#!/usr/bin/python3
"""A script that starts a Flask web application with three routes."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' message on the root route."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' message on the /hbnb route."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_troute(text):
    """Display 'C ' followed by the value of text message."""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
