from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register blueprints or routes
    from .routes import main
    app.register_blueprint(main)

    return app
