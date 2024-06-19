from flask import Blueprint
from model import models

model_api = Blueprint(
    'model',
    __name__,
    url_prefix="/api/v1"
    )

from . import errors, views