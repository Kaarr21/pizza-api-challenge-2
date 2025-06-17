from flask import Flask
from flask_migrate import Migrate
from .models import db
from .config import Config

# Importing controllers to register blueprints
from .controllers.restaurant_controller import restaurant_bp
from .controllers.pizza_controller import pizza_blueprint
from .controllers.restaurant_pizza_controller import restaurant_pizza_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    # Register routes
    app.register_blueprint(restaurant_blueprint)
    app.register_blueprint(pizza_blueprint)
    app.register_blueprint(restaurant_pizza_blueprint)

    return app

app = create_app()
