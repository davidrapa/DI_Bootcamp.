from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    address_city = StringField('Address City', validators=[DataRequired()])
    submit = SubmitField('Log In')
