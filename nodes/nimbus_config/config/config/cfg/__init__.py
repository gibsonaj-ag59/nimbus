from flask import Blueprint

configs_api = Blueprint(
    'configs',
    __name__,
    url_prefix="/api/v1/configs"
    )

from . import errors, views