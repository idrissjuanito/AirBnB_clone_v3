#!/usr/bin/python3
""" handle route views """
from api.v1.views import app_views


@app_views.route("/status")
def api_status():
    """ reponds with a status of the api """
    return {"status": "OK"}
