#!/usr/bin/python3
'''flask for the website'''

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    '''send filters'''
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Close database or file storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
