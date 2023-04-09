from flask import Flask, render_template, request
import psycopg2
from faker import Faker
import json

# Create the Flask application
app = Flask(__name__)

# Create the Faker object
fake = Faker()

# Set up the database connection
db = psycopg2.connect(
    host="localhost",
    port="5432",
    database="fake_data_generator",
    user="postgres",
    password="1234"
)

# Define the home page route
@app.route("/")
def home():
    return render_template("home.html")

# Define the generate data route
@app.route("/generate_data", methods=["POST"])
def generate_data():
    # Get the form data from the request
    data_type = request.form["data_type"]
    num_records = int(request.form["num_records"])

    # Generate the fake data
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

    # Store the fake data in the database
    cursor = db.cursor()
    for item in fake_data:
        cursor.execute("INSERT INTO fake_data (data_type, fake_data) VALUES (%s, %s)", (data_type, item))
    db.commit()

    # Render the results page with the generated data
    return render_template("results.html", data=fake_data)

# Define the retrieve data route
@app.route("/retrieve_data", methods=["GET"])
def retrieve_data():
    # Retrieve the fake data from the database
    cursor = db.cursor()
    cursor.execute("SELECT fake_data FROM fake_data")
    results = cursor.fetchall()

    # Convert the results to a list of strings
    data = [result[0] for result in results]

    # Return the data as JSON
    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)
