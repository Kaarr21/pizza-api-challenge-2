from flask import Blueprint, jsonify
from server.models import Pizza

pizza_blueprint = Blueprint('pizza_blueprint', __name__, url_prefix='/pizzas')

@pizza_blueprint.route('', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([
        {
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        } for pizza in pizzas
    ])
