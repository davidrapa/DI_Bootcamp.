from flask import render_template, request
import json
from app import app
from forms import AddCity

list_of_cities = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddCity()
    if request.method == 'POST' and form.validate_on_submit():
        city_name = form.name.data
        city_country = form.country.data
        city_inhabitants = form.inhabitants.data
        city_area = form.area.data
        city_details = {'name': city_name, 'country': city_country, 'inhabitants': city_inhabitants, 'area': city_area}
        list_of_cities.append(city_details)
        with open('cities_around_the_world.json', 'w') as f:
            json.dump(list_of_cities, f)
    return render_template('index.html', form=form, cities=list_of_cities)
