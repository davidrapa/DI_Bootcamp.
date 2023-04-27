from flask import render_template, redirect, url_for
from . import films_blueprint
from .forms import AddFilmForm, AddDirectorForm
from .models import Film, Director, Country, Category, db

@films_blueprint.route('/homepage/')
def homepage():
    films = Film.query.all()
    return render_template('homepage.html', films=films)

@films_blueprint.route('/addFilm/', methods=['GET', 'POST'])
def addFilm():
    form = AddFilmForm()

    if form.validate_on_submit():
        film = Film(
            title=form.title.data,
            release_date=form.release_date.data,
            created_in_country=form.created_in_country.data,
            available_in_countries=form.available_in_countries.data,
            categories=form.categories.data,
            directors=form.directors.data
        )
        db.session.add(film)
        db.session.commit()
        return redirect(url_for('films.homepage'))

    return render_template('film/addFilm.html', form=form)

@films_blueprint.route('/addDirector/', methods=['GET', 'POST'])
def addDirector():
    form = AddDirectorForm()

    if form.validate_on_submit():
        director = Director(
            first_name=form.first_name.data,
            last_name=form.last_name.data
        )
        db.session.add(director)
        db.session.commit()
        return redirect(url_for('films.homepage'))

    return render_template('director/addDirector.html', form=form)
