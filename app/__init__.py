from flask import Flask
from pathlib import Path

def create_app():
    app = Flask(__name__)
    
    # Ensure the instance folder exists
    Path("instance").mkdir(exist_ok=True)
    
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main)
    
    return app 