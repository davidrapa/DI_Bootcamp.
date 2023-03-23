from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'

class CVForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Age')
    experience = TextAreaField('Experience')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CVForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        experience = form.experience.data
        return render_template('cv.html', first_name=first_name, last_name=last_name, age=age, experience=experience)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
