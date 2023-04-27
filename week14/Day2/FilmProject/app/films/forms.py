from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField

from .models import Country, Category, Director


class AddFilmForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    release_date = DateField('Release Date', format='%Y-%m-%d', validators=[DataRequired()])
    created_in_country = QuerySelectField('Created In', query_factory=lambda: Country.query, allow_blank=False)
    available_in_countries = QuerySelectMultipleField('Available In', query_factory=lambda: Country.query)
    categories = QuerySelectMultipleField('Category', query_factory=lambda: Category.query)
    directors = QuerySelectMultipleField('Director', query_factory=lambda: Director.query)
    submit = SubmitField('Add Film')


class AddDirectorForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Add Director')
