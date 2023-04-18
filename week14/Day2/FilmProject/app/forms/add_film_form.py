from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired

from app.models.country import Country
from app.models.category import Category
from app.models.director import Director

class AddFilmForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    release_date = DateField('Release Date', format='%m/%d/%Y', validators=[DataRequired()])
    created_in_country = SelectField('Created In', coerce=int, validators=[DataRequired()])
    available_in_countries = SelectMultipleField('Available In', coerce=int, validators=[DataRequired()])
    categories = SelectMultipleField('Categories', coerce=int, validators=[DataRequired()])
    directors = SelectMultipleField('Directors', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Film')

    def __init__(self):
        super(AddFilmForm, self).__init__()
        self.created_in_country.choices = [(c.id, c.name) for c in Country.query.order_by('name')]
        self.available_in_countries.choices = [(c.id, c.name) for c in Country.query.order_by('name')]
        self.categories.choices = [(c.id, c.name) for c in Category.query.order_by('name')]
        self.directors.choices = [(d.id, f"{d.first_name} {d.last_name}") for d in Director.query.order_by('last_name', 'first_name')]
