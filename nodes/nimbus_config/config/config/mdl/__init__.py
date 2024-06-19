from flask import Blueprint

model_api = Blueprint(
    'model',
    __name__,
    url_prefix="/api/v1/models"
    )

from . import errors, views