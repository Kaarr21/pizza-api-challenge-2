from flask import Blueprint, jsonify, request
from server.models import db, RestaurantPizza, Pizza, Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__, url_prefix='/restaurant_pizzas')

@restaurant_pizza_bp.route('', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Basic validations
    if price is None or not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be between 1 and 30']}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({'errors': ['Invalid restaurant or pizza ID']}), 400

    RestaurantPizza= RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(RestaurantPizza)
    db.session.commit()

    return jsonify({
        'id': RestaurantPizza.id,
        'price': RestaurantPizza.price,
        'pizza_id': pizza.id,
        'restaurant_id': restaurant.id,
        'pizza': {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        },
        'restaurant': {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        }
    }), 201
