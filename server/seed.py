from server.app import app
from server.models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():
    print(" Seeding data...")

    # Clear tables first
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create Pizzas
    pizza1 = Pizza(name="Boerwores", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    pizza3 = Pizza(name="Hawaiian", ingredients="Dough, Tomato Sauce, Cheese, Pineapple, Ham")

    db.session.add_all([pizza1, pizza2, pizza3])
    db.session.commit()

    # Create Restaurants
    rest1 = Restaurant(name="Mama's Pizza", address="123 Main St")
    rest2 = Restaurant(name="Tony's Pizza", address="456 Side Ave")
    rest3 = Restaurant(name="Kiki's Pizza", address="789 Market Rd")

    db.session.add_all([rest1, rest2, rest3])
    db.session.commit()

    # Create RestaurantPizzas
    rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=rest1.id)
    rp2 = RestaurantPizza(price=12, pizza_id=pizza2.id, restaurant_id=rest1.id)
    rp3 = RestaurantPizza(price=9, pizza_id=pizza3.id, restaurant_id=rest2.id)

    db.session.add_all([rp1, rp2, rp3])
    db.session.commit()

    print("✅ Done seeding!")
