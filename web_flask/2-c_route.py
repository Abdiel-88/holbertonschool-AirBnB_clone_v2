#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

# Flask automatically considers strict_slashes to be True; setting it to False globally.
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
