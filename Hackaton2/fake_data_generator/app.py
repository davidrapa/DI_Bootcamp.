from flask import Flask, render_template, request
import psycopg2
from faker import Faker
import json


app = Flask(__name__)


fake = Faker()

# set un data
db = psycopg2.connect(
    host="localhost",
    port="5432",
    database="fake_data_generator",
    user="postgres",
    password="1234"
)

#  home page route
@app.route("/")
def home():
    return render_template("home.html")

# generate data route
@app.route("/generate_data", methods=["POST"])
def generate_data():
    # Get the form data from the request
    data_type = request.form["data_type"]
    num_records = int(request.form["num_records"])

    #  fake data Generated item
    fake_data = []
    for i in range(num_records):
        if data_type == "name":
            fake_data.append(fake.name())
        elif data_type == "address":
            fake_data.append(fake.address())
        elif data_type == "phone":
            fake_data.append(fake.phone_number())
        elif data_type == "email":
            fake_data.append(fake.email())


    cursor = db.cursor()
    for item in fake_data:
        cursor.execute("INSERT INTO fake_data (data_type, fake_data) VALUES (%s, %s)", (data_type, item))
    db.commit()


    return render_template("results.html", data=fake_data)


@app.route("/retrieve_data", methods=["GET"])
def retrieve_data():

    cursor = db.cursor()
    cursor.execute("SELECT fake_data FROM fake_data")
    results = cursor.fetchall()


    data = [result[0] for result in results]


    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)
