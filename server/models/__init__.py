from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import all model classes so Alembic can detect them
from .restaurant import Restaurant
from .pizza import Pizza
from .restaurant_pizza import RestaurantPizza
