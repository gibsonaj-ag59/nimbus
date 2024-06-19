from api.open_api import api
from flask import request
import requests
import json
import os

device = os.environ.get('DEVICE_NAME', None)

@api.route("/" + device, methods=['GET'])
def request_data():
    query = '?' + request.query_string.decode()
    if query == '?':
        response = requests.get(
            f'http://{device}.nimbus:5556/api/v1/{device}',
            )
        return json.dumps(response.json())
    else:
        response = requests.get(
            f'http://{device}.nimbus:5556/api/v1/{device}{query}',
            )
        return json.dumps(response.json())