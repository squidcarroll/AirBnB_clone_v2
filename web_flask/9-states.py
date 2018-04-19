#!/usr/bin/python3
''' list sstates '''

from flask import Flask, render_template
from models import storage, State, City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def listStates(state_id=None):
    if state_id is None:
        states = storage.all(State)
        cities = None
    else:
        states = [obj for obj in storage.all(State) if obj.id == state_id]
        if not states:
            states = None
            cities = None
        else:
            cities = [obj for obj in storage.all(City) if obj.state_id == state_id]

    return render_template('9-states.html', states=states, cities=cities)


@app.teardown_appcontext
def tear_down(exceptions):
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
