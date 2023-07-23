#!/usr/bin/python3
"""-*- coding: utf-8 -*-"""

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # Replace underscores with spaces in the text variable
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    # Replace underscores with spaces in the text variable
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # Check if n is an integer
    if isinstance(n, int):
        return render_template('6-number_template.html', number=n)
    else:
        return 'Not Found', 404


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    # Check if n is an integer
    if isinstance(n, int):
        odd_or_even = 'odd' if n % 2 != 0 else 'even'
        return render_template('6-number_odd_or_even.html',
                               number=n, odd_even=odd_or_even)
    else:
        return 'Not Found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
