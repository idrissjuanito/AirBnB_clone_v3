#!/usr/bin/python3
"""
Views related to states
"""
from flask import abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.get("/states", strict_slashes=False)
def all_states():
    """ fetches and delivers all state objects """
    json_obj = []
    states = storage.all(State)

    for state in states.values():
        json_obj.append(state.to_dict())
    return json_obj


@app_views.get("/states/<state_id>", strict_slashes=False)
def state_cities(state_id):
    """ get all cities in a state object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.cities


@app_views.delete("/states/<state_id>")
def del_state(state_id):
    """ Deletes a state by id """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return {}, 200


@app_views.post("/states", strict_slashes=False)
def new_state():
    """ handles post request to create new state object """
    try:
        data = request.get_json()
        if "name" not in data.keys():
            return "Missing name", 400
        state = State(data['name'])
        setattr(state, 'name', data['name'])
        storage.new(state)
        storage.save()
        return state.to_dict(), 201
    except Exception:
        return "Not a JSON", 400


@app_views.put("/states/<state_id>", strict_slashes=False)
def update_state(state_id):
    """ updates a state object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    try:
        data = request.get_json()
        setattr(state, 'name', data['name'])
        storage.save()
        return state.to_dict(), 200
    except Exception:
        return "Not a JSON", 400
