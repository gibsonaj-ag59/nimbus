from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests
import os
import json


db = SQLAlchemy()
_config_name = os.environ.get('CONFIG_NAME', 'v_model')
_model_name = os.environ.get('MODEL_NAME')

def create_app():
    app = Flask(__name__)
    cfg_obj = requests.get(
        f'http://config.vitruvius:5555/api/v1/configs/get_config/{_config_name}'
    )
    mdl_obj = requests.get(
        f'http://config.vitruvius:5555/api/v1/models/get_model/{_model_name}'
    )
    test_data = requests.get(
        f'http://config.vitruvius:5555/api/v1/tests/get_test/{_model_name}_data'
    )
    app.config.update(cfg_obj.json())
    print(mdl_obj)
    from .models import DataModel
    DataModel = DataModel.init_model(mdl_obj.json())

    from .ddm import DeviceDataManagement
    ddm = DeviceDataManagement(db, app)
    ddm.create_device_tables(db, app)

    for _ in json.loads(test_data.text)["values"]:
        model = DataModel(**_)
        ddm.insert_test_data(app, db, model)

    from .api import v_model_api
    app.register_blueprint(v_model_api)

    return app