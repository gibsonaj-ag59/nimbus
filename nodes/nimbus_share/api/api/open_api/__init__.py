from flask import Blueprint

api = Blueprint(
    'napi',
    __name__, 
    url_prefix='/api/v1'
    )

from . import errors, views
