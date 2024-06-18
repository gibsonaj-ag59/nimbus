from v_config.v_tst import v_test_api
from ..v_redis import vr
import json

# Get Config
@v_test_api.route('/get_test/<string:test_name>', methods=['GET'])
def get_test(test_name):
    result = vr.get(test_name)
    return json.loads(result)