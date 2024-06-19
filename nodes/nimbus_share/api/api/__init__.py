from flask import Flask
import requests
import os

def create_app():
    app = Flask(__name__)
    config_name = os.environ.get('CONFIG_NAME', 'default')
    cfg_obj = requests.get(
        f'http://config.nimbus:5555/api/v1/configs/get_config/{config_name}'
        )
    app.config.update(cfg_obj.json())

    from api.open_api import api
    app.register_blueprint(api)

    return app

