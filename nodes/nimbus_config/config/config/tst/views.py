from config.tst import test_api
from ..redis import vr
import json

# Get Config
@test_api.route('/get_test/<string:test_name>', methods=['GET'])
def get_test(test_name):
    result = vr.get(test_name)
    return json.loads(result)