from flask import Blueprint

from . import errors

btstrp_srvc = Blueprint(
    'btstrp',
    '__name__',
    url_prefix='/api/v1/btstrp'
)

from . import views