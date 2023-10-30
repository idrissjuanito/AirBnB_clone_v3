#!/usr/bin/python3
"""
Views related to cities
"""
from flask import abort, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


@app_views.get("/cities/<city_id>", strict_slashes=False)
def one_city(city_id):
    """ gets a city record """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return city.to_dict()


@app_views.get("/cities/<state_id>/cities", strict_slashes=False)
def city_cities(state_id):
    """ Gets a city by it's id """
    state = storage.get(State, city_id)
    if state is None:
        abort(404)
    return city.cities


@app_views.delete("/cities/<city_id>")
def del_city(city_id):
    """ Deletes a city by id """
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return {}, 200


@app_views.post("/states/<state_id>/cities", strict_slashes=False)
def new_city(state_id):
    """ handles post request to create new city object """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    try:
        data = request.get_json()
        if "name" not in data.keys():
            return "Missing name", 400
        city = City()
        setattr(city, 'name', data['name'])
        setattr(city, 'state_id', state_id)
        storage.new(city)
        storage.save()
        return city.to_dict(), 201
    except Exception:
        return "Not a JSON", 400


@app_views.put("/cities/<city_id>", strict_slashes=False)
def update_city(city_id):
    """ updates a city object """
    city = storage.get(city, city_id)
    if city is None:
        abort(404)
    try:
        data = request.get_json()
        setattr(city, 'name', data['name'])
        storage.save()
        return city.to_dict(), 200
    except Exception:
        return "Not a JSON", 400
