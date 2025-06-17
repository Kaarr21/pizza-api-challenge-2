from flask import Blueprint, jsonify, request
from server.models import db, Restaurant, RestaurantPizza

restaurant_blueprint = Blueprint('restaurant_blueprint', __name__, url_prefix='/restaurants')

@restaurant_blueprint.route('', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([
        {
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        } for restaurant in restaurants
    ])

@restaurant_blueprint.route('/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [
            {
                'id': RestaurantPizza.pizza.id,
                'name': RestaurantPizza.pizza.name,
                'ingredients':RestaurantPizza.pizza.ingredients
            } for RestaurantPizza in restaurant.restaurant_pizzas
        ]
    })

@restaurant_blueprint.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    db.session.delete(restaurant)
    db.session.commit()
    return '', 204
