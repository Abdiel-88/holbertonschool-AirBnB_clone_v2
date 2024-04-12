#!/usr/bin/python3
"""
A simple Flask web application that lists states and cities from storage.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False  # The Flask application instance setting.


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states(id):
    """
    Serves a webpage that lists all states or the cities of a specific state.
    If an ID is provided, the cities of that state are displayed.
    If no ID is provided, all states are listed.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)

    if id is not None:
        state = next((state for state in states if state.id == id), None)
        if state:
            cities = sorted(state.cities, key=lambda city: city.name)
            return render_template('9-state.html', state=state, cities=cities)
        return render_template('9-not_found.html'), 404
    else:
        return render_template('9-states.html', states=states)


@app.teardown_appcontext
def close_storage(exception):
    """
    Closes the storage on teardown,
    ensuring no leftover transactions or connections.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
