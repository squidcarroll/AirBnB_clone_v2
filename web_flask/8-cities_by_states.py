#!/usr/bin/pyton3
'''list cities by states'''

from flask import Flask, render_template
from models import storage, State, City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def list_states_and_cities():
    return render_template(
        '8-cities_by_states.html',
        st=storage.all(State),
        ct=storage.all(City)
    )


@app.teardown_appcontext
def tear_down(exceptions):
    storage.close()

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
