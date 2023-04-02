from flask import Flask, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

# Please change the strucure as we learned
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
fake = Faker()


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phonenumbers = db.relationship('PhoneNumber', backref='owner', lazy=True)

    def __repr__(self):
        return f"Person(id={self.id}, name='{self.name}', email='{self.email}', address='{self.address}')"


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)

    def __repr__(self):
        return f"PhoneNumber(id={self.id}, number='{self.number}', owner_id={self.owner_id})"


@app.route("/")
def home():
    return "Welcome to the phonebook!"


def add_fake_person():
    with app.app_context():
        name = fake.name()
        email = fake.email()
        address = fake.address()
        person = Person(name=name, email=email, address=address)
        db.session.add(person)
        db.session.commit()
        return person


def add_fake_phonenumber(person):
    with app.app_context():
        number = fake.phone_number()
        phonenumber = PhoneNumber(number=number, owner=person)
        db.session.add(phonenumber)
        db.session.commit()
        return phonenumber


@app.route("/person/<phonenumber>")
def get_person_by_phonenumber(phonenumber):
    person = Person.query.join(PhoneNumber).filter(PhoneNumber.number == phonenumber).first()
    if person:
        return render_template('person.html', person=person)
    else:
        return abort(404)


@app.route("/person/<name>")
def get_person_by_name(name):
    people = Person.query.filter_by(name=name).all()
    if people:
        return render_template('people.html', people=people)
    else:
        return abort(404)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        for _ in range(10):
            person = add_fake_person()
            for _ in range(random.randint(1, 4)):
                add_fake_phonenumber(person)
    app.run(debug=True)
