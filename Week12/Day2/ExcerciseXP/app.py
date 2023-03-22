from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'papapa'

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
