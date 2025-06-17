#  Pizza Restaurant API

A RESTful API built with Flask for managing restaurants, pizzas, and their relationships. This project allows you to perform CRUD operations on restaurants and pizzas, and associate pizzas with specific restaurants via a join model.

---

##  Project Structure

##  Features

- View all restaurants or a single restaurant with its pizzas.
- View all pizzas.
- Add a new pizza to a restaurant with pricing.
- Delete a restaurant.
- Full API error handling.
- Modular MVC structure.

---

##  Tech Stack

- Python 3.8+
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite (default DB)

---

##  Setup Instructions

### 1. Clone the Repo

```bash
git clone <your-repo-url>
cd pizza-api-challenge-2

2. Create and Activate Virtual Environment
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate

3.  Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

4. Set Up Environment Variables

FLASK_APP=server.app
FLASK_ENV=development

Database Setup
1. Initialize Migrations
flask db init

2. Generate Migrations
flask db migrate -m "Initial migration"

3. Apply Migrations
flask db 

4. Seed the Database
python server/seed.py

Testing the API with Postman
Launch your Flask server:
flask run

Code Organization
Models: SQLAlchemy models defining tables and relationships.

Controllers: Blueprint-based route logic for each model.

Migrations: DB versioning using Flask-Migrate.

Seed: Initial sample data for dev/testing.
