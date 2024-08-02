#!/usr/bin/python3
"""A script that starts a Flask web application with seven routes."""
from flask import Flask, render_template

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
    """Display 'C ' followed by the value of text as message."""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_troute(text):
    """Display 'Python ' followed by the value of text as message."""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_nroute(n):
    """Display 'n is a number' only if n is an integer as message."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_ntemplate(n):
    """Display a HTML page only if n is an integer as message."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer,
    showing if it's odd or even."""
    odd_or_even = "odd" if n % 2 else "even"
    return render_template('6-number_odd_or_even.html', n=n,
                           odd_or_even=odd_or_even)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
