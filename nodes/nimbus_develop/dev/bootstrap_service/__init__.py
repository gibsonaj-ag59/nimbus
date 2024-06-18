from flask import Flask

def create_app():
    app = Flask('__name__')

    from bootstrap_service.v_api import btstrp_srvc
    app.register_blueprint(btstrp_srvc)

    return app