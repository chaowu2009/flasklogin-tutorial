"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()



def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    #app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost/database1"
    app.config ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sample.db"
    app.config['SECRET_KEY'] = "xxxxx7x88"

    # Initialize Plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth
        from .assets import compile_static_assets

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()

        # Compile static assets
        if app.config['FLASK_ENV'] == 'development':
            compile_static_assets(app)

        return app
