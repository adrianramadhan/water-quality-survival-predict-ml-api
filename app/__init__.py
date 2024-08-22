from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints or configure extensions here
    # Example: 
    # from .controllers.water_quality import water_quality_bp
    # app.register_blueprint(water_quality_bp)

    return app
