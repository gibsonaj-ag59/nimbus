from flask import Blueprint
from v_model import models

v_model_api = Blueprint(
    'v_model',
    __name__,
    url_prefix="/api/v1"
    )

from . import errors, views