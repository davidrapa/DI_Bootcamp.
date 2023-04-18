from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.film import Film
from app.models.country import Country
from app.models.category import Category
from app.models.director import Director
from app.forms.add_film_form import AddFilmForm

@app.route('/films/addFilm', methods=['GET', 'POST'])
def add_film():
    form = AddFilmForm()
    if form.validate_on_submit():
        title = form.title.data
        release_date = form.release_date.data
        created_in_country_id = form.created_in_country.data
        available_in_country_ids = form.available_in_countries.data
        category_ids = form.categories.data
        director_ids = form.directors.data

        created_in_country = Country.query.get(created_in_country_id)
        available_in_countries = Country.query.filter(Country.id.in_(available_in_country_ids)).all()
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        directors = Director.query.filter(Director.id.in_(director_ids)).all()

        film = Film(title=title, release_date=release_date, created_in_country=created_in_country,
                    available_in_countries=available_in_countries, categories=categories, directors=directors)
        db.session.add(film)
        db.session.commit()

        return redirect(url_for('homepage'))

    return render_template('film/add_film.html', form=form)
