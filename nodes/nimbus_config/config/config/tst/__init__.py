from flask import Blueprint

test_api = Blueprint(
    'test',
    __name__,
    url_prefix="/api/v1/tests"
    )

from . import errors, views