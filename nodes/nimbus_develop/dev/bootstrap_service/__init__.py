from flask import Flask

def create_app():
    app = Flask('__name__')

    from bootstrap_service.api import btstrp_srvc
    app.register_blueprint(btstrp_srvc)

    return app