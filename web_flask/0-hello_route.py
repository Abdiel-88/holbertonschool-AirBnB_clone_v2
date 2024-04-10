#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)

# Ensuring strict_slashes are False for all routes
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    """Returns 'Hello HBNB!' to the client."""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
