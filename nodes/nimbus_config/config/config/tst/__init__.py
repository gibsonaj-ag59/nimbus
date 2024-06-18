from flask import Blueprint

v_test_api = Blueprint(
    'v_test',
    __name__,
    url_prefix="/api/v1/tests"
    )

from . import errors, views