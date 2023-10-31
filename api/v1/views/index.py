#!/usr/bin/python3
""" handle route views """
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import classes


def pluralize(string):
    """ gets the plural of a string """
    if string[-1] == "y":
        return string[:-1] + "ies"
    else:
        return string + "s"


@app_views.route("/status")
def api_status():
    """ reponds with a status of the api """
    return {"status": "OK"}


@app_views.route("/stats")
def obj_stats():
    """ counts the number of records for all objects """
    obj_counts = {}
    for cls in classes.values():
        obj_key = pluralize(cls.__name__.lower())
        obj_counts[obj_key] = storage.count(cls)
    return obj_counts
