#!/usr/bin/python3
'''simple flask'''
from flask import Flask
from flask import render_template
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


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    '''return text'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def int(n):
    '''return only int'''
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def int_template(n=None):
    '''render template'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def int_odd_even(n):
    '''render template'''
    if n % 2 == 0:
        oe = "even"
    else:
        oe = "odd"
    return render_template('6-number_odd_or_even.html', n=n, oe=oe)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
