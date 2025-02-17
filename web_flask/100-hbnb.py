#!/usr/bin/python3
"""
Start a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Remove the current SQLAlchemy session after each request.
    """
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Display the HBNB page with the filters and places.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda
                       amenity: amenity.name)
    places = sorted(storage.all(Place).values(), key=lambda place: place.name)

    return render_template(
        '100-hbnb.html',
        states=states,
        cities=cities,
        amenities=amenities,
        places=places
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
