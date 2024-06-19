from config.mdl import model_api
from ..redis import vr
import json

# Get Config
@model_api.route('/get_model/<string:model_name>', methods=['GET'])
def get_config(model_name):
    result = vr.get(model_name)
    return json.loads(result)
    
    