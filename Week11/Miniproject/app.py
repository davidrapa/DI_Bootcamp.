from flask import Flask, render_template
from products_data import retrieve_all_products, retrieve_requested_product

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/products")
def products():
    all_products = retrieve_all_products()
    return render_template("products.html", products=all_products)

@app.route("/products/<product_id>")
def product_details(product_id):
    requested_product = retrieve_requested_product(product_id)
    return render_template("product_details.html", product=requested_product)

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/add_product_to_cart/<product_id>")
def add_product_to_cart(product_id):
    # Add logic to add product to cart
    return "Product added to cart"

@app.route("/delete_product_from_cart/<product_id>")
def delete_product_from_cart(product_id):
    # Add logic to delete product from cart
    return "Product deleted from cart"

if __name__ == "__main__":
    app.run(debug=True)
