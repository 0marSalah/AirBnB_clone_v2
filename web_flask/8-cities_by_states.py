#!/usr/bin/python3
""" starts a Flask web application """
from models import *
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
  states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
  citites = {}
  if storage == 'db':
    for state in states:
      for city in state.cities:
        citites[city.id] = city
  else:
    for state in states:
      citites[state.id] = state.cities
  return render_template('8-cities_by_states.html', states=states, cities=citites)

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5000')