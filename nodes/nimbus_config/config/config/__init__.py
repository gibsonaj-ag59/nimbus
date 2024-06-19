from flask import Flask
from .redis import vr


def create_app():
    app = Flask(__name__)

    from .cfg import configs_api
    app.register_blueprint(
        configs_api
        )
    from .mdl import model_api
    app.register_blueprint(
        model_api
        )
    from .tst import test_api
    app.register_blueprint(
        test_api
        )
    vr.load_configs()
    vr.load_models()
    vr.load_tests()
    return app