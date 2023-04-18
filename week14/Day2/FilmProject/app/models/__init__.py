from app import db

# Import models
from .country import Country
from .category import Category
from .film import Film
from .director import Director

# Create tables
db.create_all()
