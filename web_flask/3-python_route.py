#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """return Hello HBNB!"""
    return 'Hello HBNB|'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """display "C " followed by the variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
def pythonIsCool(text= 'is cool'):
    """display 'python' followed by the varibale text"""
    return 'python ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
