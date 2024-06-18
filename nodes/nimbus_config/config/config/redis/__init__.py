from redis import Redis
import json
import os

class VRedis(Redis):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_configs(self):
        for file in os.listdir('/app/v_config/configs/'):
            if file.endswith('.json'):
                with open(f'/app/v_config/configs/{file}', 'r') as f:
                    cfg_obj = json.load(f)
                self.set(file.split('.')[0], json.dumps(cfg_obj))

    def load_models(self):
        for file in os.listdir('/app/v_config/models/'):
            if file.endswith('.json'):
                with open(f'/app/v_config/models/{file}', 'r') as f:
                    mdl_obj = json.load(f)
                self.set(file.split('.')[0], json.dumps(mdl_obj))

    def load_tests(self):
        for file in os.listdir('/app/v_config/tests/'):
            if file.endswith('.json'):
                with open(f'/app/v_config/tests/{file}', 'r') as f:
                    test_obj = json.load(f)
                self.set(file.split('.')[0], json.dumps(test_obj))

    def save_configs(self, *config_objs):
        for config_obj in config_objs:
            self.set(config_obj['name'], json.dumps(config_obj))

vr = VRedis(
    host = os.environ.get("REDIS_HOST", "localhost"),
    port = os.environ.get("REDIS_PORT", 6379),
    username = os.environ.get("REDIS_USERNAME", "default"),
    password = os.environ.get("REDIS_PASSWORD", "CSFDcode123"),
    # ssl = os.environ.get("REDIS_SSL_VERIFY", False),
    # ssl_certfile = os.environ.get("REDIS_SSL_CERTFILE", ""),
    # ssl_keyfile = os.environ.get("REDIS_SSL_KEYFILE", ""),
    # ssl_ca_certs = os.environ.get("REDIS_SSL_CA_CERTS", "")
)