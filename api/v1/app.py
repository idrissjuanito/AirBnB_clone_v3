""" Airbnb flask api entry point """
from api.v1.views import app_views
from flask import Flask
from models import storage
app = Flask(__name__)
app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def teardown_db(exception):
    """ closes open storage connections """
    storage.close()


if __name__ == "__main__":
    from os import getenv

    HBNB_API_HOST = getenv("HBNB_API_HOST") or "0.0.0.0"
    HBNB_API_PORT = getenv("HBNB_API_PORT") or 5000
    app.run(host=HBNB_API_HOST,
            port=HBNB_API_PORT,
            threaded=True)
