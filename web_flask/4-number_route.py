#!/usr/bin/python3
"""script that starts a flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """prints a Message when / is called
    """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints a Message when /hbnb is called
    """

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """prints a Message when /c is called
    """

    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    """prints a message when /python is called
    """

    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    """prints a message when /number is called only if n is an integer
    """

    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
