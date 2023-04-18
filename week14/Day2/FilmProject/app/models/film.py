from app import db
from datetime import datetime

film_countries = db.Table('film_countries',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
    db.Column('country_id', db.Integer, db.ForeignKey('country.id'), primary_key=True)
)

film_categories = db.Table('film_categories',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)

film_directors = db.Table('film_directors',
    db.Column('film_id', db.Integer, db.ForeignKey('film.id'), primary_key=True),
    db.Column('director_id', db.Integer, db.ForeignKey('director.id'), primary_key=True)
)

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_in_country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)
    created_in_country = db.relationship('Country', backref=db.backref('films_created', lazy=True))
    available_in_countries = db.relationship('Country', secondary=film_countries, lazy='subquery', backref=db.backref('films_available', lazy=True))
    categories = db.relationship('Category', secondary=film_categories, lazy='subquery', backref=db.backref('films', lazy=True))
    directors = db.relationship('Director', secondary=film_directors, lazy='subquery', backref=db.backref('films', lazy=True))

    def __repr__(self):
        return self.title
