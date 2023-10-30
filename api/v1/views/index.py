#!/usr/bin/python3
""" handle route views """
from api.v1.views import app_views
from models import storage
from models.engine.db_storage import classes


@app_views.route("/status")
def api_status():
    """ reponds with a status of the api """
    return {"status": "OK"}

@app_views.route("/stats")
def obj_stats():
    """ counts the number of records for all objects """
    obj_counts = {}
    for cls in classes.values():
        obj_counts[cls.__name__.lower()] = storage.count(cls)
    return obj_counts
