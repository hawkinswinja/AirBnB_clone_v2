#!/usr/bin/python3
"""web app to display all available states"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def get_states(id=None):
    """return cities of a single state"""
    states = storage.all(State)
    if id is None:
        return render_template('7-states_list.html', states=states.values())
    else:
        state = states.get('State.{}'.format(id))
        return render_template('9-states.html', state=state)


@app.teardown_appcontext
def close_app(exc):
    """close current sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
