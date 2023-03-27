from flask import render_template
from __init__ import app, db
from models import User

@app.route('/')
def index():
    return render_template('index.html')
