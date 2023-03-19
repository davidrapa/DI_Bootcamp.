from flask import Flask, render_template
import json

app = Flask(__name__)

# Retrieve all products from products.json file
def retrieve_all_products():
    with open('products.json', 'r') as f:
        all_products = json.load(f)
    return all_products

# Retrieve requested product from products.json file
def retrieve_requested_product(product_id):
    with open('products.json', 'r') as f:
        all_products = json.load(f)
    for product in all_products:
        if product["ProductId"] == product_id:
            requested_product = product
            break
    return requested_product

# Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Display all products
@app.route('/products')
def products():
    all_products = retrieve_all_products()
    return render_template('products.html', products=all_products)

# Display requested product
@app.route('/products/<product_id>')
def product_details(product_id):
    requested_product = retrieve_requested_product(product_id)
    return render_template('product_details.html', product=requested_product)

if __name__ == '__main__':
    app.run(debug=True)