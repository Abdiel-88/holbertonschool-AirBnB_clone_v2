#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

# Setting strict_slashes to False globally.
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """Returns 'Hello HBNB!' to the client."""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """Returns 'HBNB' to the client."""
    return 'HBNB'

@app.route('/c/<text>')
def c_is_fun(text):
    """Returns 'C ' followed by the value of the text variable."""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def python_is_cool(text="is cool"):
    """Returns 'Python ', followed by the value of the text variable."""
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def number(n):
    """Returns 'n is a number' only if n is an integer."""
    return '{} is a number'.format(n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
