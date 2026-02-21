import os
from flask import Flask
from app.routes.health import health_bp
from app.routes.tasks import tasks_bp
from app.config import config_map



def create_app():
    app = Flask(__name__)
    env = os.environ.get("APP_ENV", "dev")  # This can be set dynamically based on environment variables or other logic
    if env not in config_map:
        raise ValueError(f"Invalid environment '{env}'. Valid options are: {list(config_map.keys())}")
    ConfigClass = config_map.get(env)

    # Register Blueprints
    app.register_blueprint(health_bp)
    app.register_blueprint(tasks_bp)
    app.config.from_object(ConfigClass)  # Load config based on environment variable
    return app

app = create_app()