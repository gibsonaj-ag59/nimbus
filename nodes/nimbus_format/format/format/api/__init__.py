from flask import Blueprint

v_format = Blueprint(
    'v_format',
    __name__,
    url_prefix='/web/v1/format'
    )

from . import errors, views