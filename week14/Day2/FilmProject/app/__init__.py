from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application
app = Flask(__name__)

# Load the configuration file
app.config.from_object('config')

# Create the database object
db = SQLAlchemy(app)

# Import the routes
from app.routes.home_routes import *
from app.routes.film_routes import *
from app.routes.director_routes import *


# Define a function to create the database tables
def create_tables():
    with app.app_context():
        db.create_all()


# Run the application and create the database tables
if __name__ == '__main__':
    create_tables()
    app.run()
