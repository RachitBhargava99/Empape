from flask import Flask
from frontend.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from frontend.dashboard.routes import dash
    app.register_blueprint(dash)

    return app
