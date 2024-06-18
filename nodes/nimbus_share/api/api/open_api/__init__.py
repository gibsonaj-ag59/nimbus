from flask import Blueprint

v_open_api = Blueprint(
    'v_api',
    __name__, 
    url_prefix='/api/v1'
    )

from . import errors, views
