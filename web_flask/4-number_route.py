#!/usr/bin/python3
"""Start a Flask web application with more complex dynamic routes"""

from flask import Flask
app = Flask(__name__)

# Enforce strict_slashes=False globally
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Return 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Display 'C <text>', with underscores replaced by spaces"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """Display 'Python <text>', with underscores replaced by spaces.
    The default value of text is 'is cool'."""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
