from flask import Flask

from config import Config

from src.route.api import api
from src.route.site import site


def create_app():
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(Config)

    app.register_blueprint(api)
    app.register_blueprint(site)

    return app
