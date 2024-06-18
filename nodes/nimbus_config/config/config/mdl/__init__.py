from flask import Blueprint

v_model_api = Blueprint(
    'v_model',
    __name__,
    url_prefix="/api/v1/models"
    )

from . import errors, views