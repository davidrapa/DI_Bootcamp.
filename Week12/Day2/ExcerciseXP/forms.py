from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class AddCity(FlaskForm):
    name = StringField('City Name', validators=[DataRequired()])
    country = StringField('City Country', validators=[DataRequired()])
    inhabitants = IntegerField('Number of Inhabitants', validators=[DataRequired()])
    area = IntegerField('City Area (in square km)', validators=[DataRequired()])
    submit = SubmitField('Add City')
