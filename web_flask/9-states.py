#!/usr/bin/python3
"""Start web application with two routings"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states_list(id):
    """
    Render template with states or
    specific state with cities if id is provided
    """
    states = storage.all(State).values()
    if id:
        state = next((s for s in states if s.id == id), None)
        return render_template('9-state.html', state=state)
    else:
        sorted_states = sorted(states, key=lambda state: state.name)
        return render_template('9-states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the SQLAlchmey session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
