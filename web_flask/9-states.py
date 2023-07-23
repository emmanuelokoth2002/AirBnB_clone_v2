#!/usr/bin/python3
"""Starts a Flask web application to display states and cities."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Closes the database session after each request.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """
    Displays a HTML page with a list of states.
    """
    states = sorted(storage.all('State').values(), key=lambda
                    state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """
    Displays a HTML page with cities of a state by ID.
    """
    state = storage.get('State', id)
    return render_template('9-states.html', state=state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
