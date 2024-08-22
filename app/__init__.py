from flask import Flask
from app.api.routes import api_bp  # Import the blueprint

def create_app():
    app = Flask(__name__)

    # Register the blueprint
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
