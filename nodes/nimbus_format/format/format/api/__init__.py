from flask import Blueprint

format = Blueprint(
    'format',
    __name__,
    url_prefix='/web/v1/format'
    )

from . import errors, views