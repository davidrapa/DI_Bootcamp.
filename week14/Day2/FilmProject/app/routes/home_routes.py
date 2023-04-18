from flask import render_template
from app import app
from app.models.film import Film

@app.route('/films/homepage')
def homepage():
    films = Film.query.all()
    return render_template('homepage.html', films=films)
