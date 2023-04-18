from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.director import Director
from app.forms.add_director_form import AddDirectorForm

@app.route('/films/addDirector', methods=['GET', 'POST'])
def add_director():
    form = AddDirectorForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data

        director = Director(first_name=first_name, last_name=last_name)
        db.session.add(director)
        db.session.commit()

        return redirect(url_for('homepage'))

    return render_template('director/add_director.html', form=form)
