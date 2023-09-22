#!/usr/bin/python3
"""Starts a Flask application on 0.0.0.0:5000"""


from flask import Flask, abort, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a simple greeting page"""

    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a page containing the string 'HBNB'"""

    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def route_c(text):
    """Returns a page about C"""

    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def rout_python(text="is cool"):
    """Returns a page about Python """

    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<n>', strict_slashes=False)
def rout_number(n):
    """Returns a page about number"""

    return ("{} is number".format(n) if n.isdigit() else abort(404))


@app.route('/number_template/<n>', strict_slashes=False)
def rout_number_template(n):
    """Returns a page about number"""

    return (render_template("5-number.html",
                            n=n) if n.isdigit() else abort(404))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
