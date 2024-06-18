from v_config.v_cfg import v_configs_api
from flask import request
from ..v_redis import vr
import json

# Get Config
@v_configs_api.route('/get_config/<string:config_name>', methods=['GET'])
def get_config(config_name):
    result = vr.get(config_name)
    return json.loads(result)
    
@v_configs_api.route('/save_config', methods=['POST'])
def save_config():
    config_obj = json.loads(request.json)
    vr.save_configs(config_obj)
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

