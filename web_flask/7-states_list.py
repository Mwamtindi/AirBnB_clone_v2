#!/usr/bin/python3
"""module starts a Flask web application and displays a list of states"""
from flask import Flask, render_template
from models import *
from models import storage
app = Flask(__name__)
"""Displays a list of states sorted alphabetically."""


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a HTML page with the states listed in alphabetical order"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown and remove current SQLAlchemy ses"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
