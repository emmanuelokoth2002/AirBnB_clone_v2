#!/usr/bin/python3
"""Starts a Flask web application to display an
   HTML page with Airbnb filters."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """
    Closes the database session after each request.
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Displays an HTML page with Airbnb filters.
    """
    states = sorted(storage.all('State').values(), key=lambda
                    state: state.name)
    cities = sorted(storage.all('City').values(), key=lambda city: city.name)
    amenities = sorted(storage.all('Amenity').values(), key=lambda
                       amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=states,
                           cities=cities, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
