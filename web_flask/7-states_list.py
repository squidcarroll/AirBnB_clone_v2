#!/usr/bin/python3
''' list states '''

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def listStates():
    ''' list states '''
    return render_template('7-states_list.html', st=storage.all(State))


@app.teardown_appcontext
def tear_down(exceptions):
    storage.close()

if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
