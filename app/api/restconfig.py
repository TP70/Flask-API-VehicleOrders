import logging

from flask_restplus import Api
from app import settings

log = logging.getLogger(__name__)

api = Api(
    version="1.0",
    title="Vehicle Order API",
    description="API that stores and retrieve information of a vehicle order",
)


@api.errorhandler
def default_error_handler(e):
    message = "An unhandled exception occurred."
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {"message": message}, 500
