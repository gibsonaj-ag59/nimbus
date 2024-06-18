from flask import Blueprint

v_configs_api = Blueprint(
    'v_configs',
    __name__,
    url_prefix="/api/v1/configs"
    )

from . import errors, views