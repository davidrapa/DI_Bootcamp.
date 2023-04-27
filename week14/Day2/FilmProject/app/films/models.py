from datetime import date
from app import db

class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)

films_categories = db.Table('films_categories',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

films_directors = db.Table('films_directors',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
    db.Column('director_id', db.Integer, db.ForeignKey('director.id'), primary_key=True)
)

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    release_date = db.Column(db.Date, default=date.today, nullable=False)
    created_in_country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    created_in_country = db.relationship('Country', backref='films_created')
    available_in_countries = db.relationship('Country', secondary='films_available', backref=db.backref('films_available', lazy='dynamic'))
    categories = db.relationship('Category', secondary=films_categories, backref=db.backref('films', lazy='dynamic'))
    directors = db.relationship('Director', secondary=films_directors, backref=db.backref('films', lazy='dynamic'))
