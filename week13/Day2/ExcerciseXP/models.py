from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    street = db.Column(db.String(100), nullable=False)
    suite = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    zipcode = db.Column(db.String(100), nullable=False)
