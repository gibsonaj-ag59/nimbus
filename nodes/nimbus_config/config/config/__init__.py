from flask import Flask
from .v_redis import vr


def create_app():
    app = Flask(__name__)

    from .v_cfg import v_configs_api
    app.register_blueprint(
        v_configs_api
        )
    from .v_mdl import v_model_api
    app.register_blueprint(
        v_model_api
        )
    from .v_tst import v_test_api
    app.register_blueprint(
        v_test_api
        )
    vr.load_configs()
    vr.load_models()
    vr.load_tests()
    return app