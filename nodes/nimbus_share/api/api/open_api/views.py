from v_api.v_open_api import v_open_api
from flask import request
import requests
import json
import os

device = os.environ.get('DEVICE_NAME', None)

@v_open_api.route("/" + device, methods=['GET'])
def request_data():
    query = '?' + request.query_string.decode()
    if query == '?':
        response = requests.get(
            f'http://{device}.vitruvius:5556/api/v1/{device}',
            )
        return json.dumps(response.json())
    else:
        response = requests.get(
            f'http://{device}.vitruvius:5556/api/v1/{device}{query}',
            )
        return json.dumps(response.json())