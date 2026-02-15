from flask import Flask
from app.routes.health import health_bp
from app.routes.tasks import tasks_bp


def create_app():
    app = Flask(__name__)

    # Register Blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(tasks_bp)

    return app