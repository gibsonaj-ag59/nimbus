from flask import Flask
import requests
import os

def create_app():
    app = Flask(__name__)
    config_name = os.environ.get('CONFIG_NAME', 'format')
    cfg_obj = requests.get(
        f'http://config.nimbus:5555/api/v1/configs/get_config/{config_name}'
        )
    deps = [
        {'styles':
         [
             'bootstrap.min.css'
         ]
        },
        {'scripts':
         [
             'bootstrap.bundle.min.js',
             'v.format.ingest.js'
         ]
        }
    ]
    for d in deps:
        for k, v in d.items():
            for file in v:
                f = requests.get(f"http://dev.nimbus:5552/api/v1/btstrp/get/{k}/{file}")
                write_tmp(f, f'{k}/{file}')

    app.config.update(cfg_obj.json())

    from .api import format
    app.register_blueprint(format)

    return app

def write_tmp(resp, path):
    with open(f'/app/format/static/{path}', 'w') as f:
        f.write(resp.text)