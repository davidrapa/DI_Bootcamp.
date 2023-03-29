from flask import render_template, flash, redirect, url_for
from app import app, db
from models import User
from forms import LoginForm


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/check_user/<name>')
def check_user(name):
    user = User.query.filter_by(name=name).first()
    if user:
        return True
    else:
        return False


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        address_city = form.address_city.data
        if not name.isalpha() or not address_city.isalpha():
            flash('Error: Please enter valid credentials', category='error')
            return redirect(url_for('login'))
        if check_user(name):
            flash('You are now logged in!', category='success')
            return redirect(url_for('index'))
        else:
            flash('You need to sign up first!', category='warning')
            return redirect(url_for('add_user'))
    return render_template('login.html', form=form)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        address_city = form.address_city.data
        if not name.isalpha() or not address_city.isalpha():
            flash('Error: Please enter valid credentials', category='error')
            return redirect(url_for('add_user'))
        if check_user(name):
            flash('You already have an account! Please log in.', category='warning')
            return redirect(url_for('login'))
        else:
            user = User(name=name, address_city=address_city)
            db.session.add(user)
            db.session.commit()
            flash('You have successfully signed up!', category='success')
            return redirect(url_for('index'))
    return render_template('add_user.html', form=form)
