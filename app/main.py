import logging.config

import os
from flask import Flask, Blueprint
from app import settings
from app.api.order.controllers.vehicle_order import ns as vehicle_orders_namespace
from app.api.restconfig import api

logging_conf_path = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "../logging.conf")
)
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


def init():
    app = Flask(__name__)
    app.config["SERVER_NAME"] = settings.FLASK_SERVER_NAME
    app.config["SWAGGER_UI_DOC_EXPANSION"] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    app.config["RESTPLUS_VALIDATE"] = settings.RESTPLUS_VALIDATE
    app.config["RESTPLUS_MASK_SWAGGER"] = settings.RESTPLUS_MASK_SWAGGER
    app.config["ERROR_404_HELP"] = settings.RESTPLUS_ERROR_404_HELP

    blueprint = Blueprint("api", __name__, url_prefix="/api")
    api.init_app(blueprint)
    api.add_namespace(vehicle_orders_namespace)
    app.register_blueprint(blueprint)

    return app


def main():
    app = init()
    log.info(f">>>>> Starting development server at http://{app.config['SERVER_NAME']}/api/ <<<<<")
    app.run(debug=settings.FLASK_DEBUG)


if __name__ == "__main__":
    main()
