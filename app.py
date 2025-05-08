from flask import Flask
from app.routes import main  # Import the blueprint
import os
print("Templates directory:", os.path.join(os.getcwd(), "templates"))

def create_app():
    app = Flask(__name__, template_folder="templates")  # Explicitly set the template folder
    app.config["DEBUG"] = True  # Enable debug mode

    # Register the blueprint
    app.register_blueprint(main)

    return app