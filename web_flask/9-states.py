#!/usr/bin/python3
"""Start web application with two routings"""

from flask import Flask, render_template, abort
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states_list(id):
    """
    Render template with states or a
    specific state with cities if id is provided.
    """
    if id:
        state = storage.all(State).get('State.' + id)
        if state:
            # Sort cities of the state by name if using DBStorage
            cities = sorted(state.cities, key=lambda city: city.name) if hasattr(state, 'cities') else []
            return render_template('9-state.html', state=state, cities=cities)
        else:
            abort(404, description="Not found")
    else:
        states = storage.all(State).values()
        # Sort states by name
        sorted_states = sorted(states, key=lambda state: state.name)
        return render_template('9-states.html', states=sorted_states)


@app.teardown_appcontext
def close_storage(exception):
    """Closes the SQLAlchmey session or FileStorage."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
