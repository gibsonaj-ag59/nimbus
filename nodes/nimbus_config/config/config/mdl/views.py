from v_config.v_mdl import v_model_api
from ..v_redis import vr
import json

# Get Config
@v_model_api.route('/get_model/<string:model_name>', methods=['GET'])
def get_config(model_name):
    result = vr.get(model_name)
    return json.loads(result)
    
    