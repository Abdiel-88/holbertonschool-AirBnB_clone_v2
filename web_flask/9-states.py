#!/usr/bin/python3
'''A simple Flask web application.
'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', defaults={'id': None})
@app.route('/states/<id>')
def states(id):
    '''
    The states page. Render states
    and optionally cities of a specific state.
    '''
    all_states = sorted(storage.all(State).values(), key=lambda x: x.name)
    state = next((s for s in all_states if s.id == id), None)

    if state:
        # Sort cities in the selected state by name
        cities = sorted(state.cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    elif id is None:
        # Display all states if no specific ID is provided
        return render_template('9-states.html', states=all_states)
    else:
        # Return a 404 page if the state is not found
        return render_template('9-not_found.html'), 404


@app.teardown_appcontext
def flask_teardown(exc):
    '''Close the database or file storage system at the end of the request.'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
