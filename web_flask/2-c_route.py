#!/usr/bin/python3
'''simple flask'''
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    ''' hello '''
    return 'Hello, HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnh():
    '''hbnbpage'''
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''return teext'''
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
