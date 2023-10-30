#!/usr/bin/python3
"""
Views related to states
"""
from flask import abort, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states")
def all_states():
    """ fetches and delivers all state objects """
    json_obj = []
    states = storage.all(State)

    for state in states.values():
        json_obj.append(state.to_dict())
    return json_obj

@app_views.route("/states/<state_id>")
def one_state(state_id):
    """ Gets a state by it's id """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return state.to_dict()

@app_views.route("/states/<state_id>")
def del_state(state_id):
    """ Deletes a state by id """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    return {}, 200
