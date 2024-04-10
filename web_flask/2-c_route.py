#!/usr/bin/python3
"""Start a Flask web application with dynamic route"""

from flask import Flask
app = Flask(__name__)

# Setting strict_slashes to False globally
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Return 'Hello HBNB!' for the root route"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return 'HBNB' for the /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Return 'C <text>', and replace underscore with space in <text>"""
    text_no_underscore = text.replace('_', ' ')
    return 'C {}'.format(text_no_underscore)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
