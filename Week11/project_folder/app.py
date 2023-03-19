from flask import Flask, render_template, url_for

from products_data import retrieve_all_products, retrieve_requested_product

app = Flask(__name__)

# Set up some global variables
cart_items = []

# Define routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/products')
def products():
    all_products = retrieve_all_products()
    return render_template('products.html', products=all_products)


@app.route('/products/<product_id>')
def product_details(product_id):
    requested_product = retrieve_requested_product(product_id)
    return render_template('product_details.html', product=requested_product)


@app.route('/cart')
def cart():
    total_price = 0
    for item in cart_items:
        total_price += item['Price']

    return render_template('cart.html', cart_items=cart_items, total_price=total_price)


@app.route('/add_product_to_cart/<product_id>')
def add_to_cart(product_id):
    requested_product = retrieve_requested_product(product_id)
    cart_items.append(requested_product)
    return "Product added to cart!"


@app.route('/delete_product_from_cart/<product_id>')
def delete_from_cart(product_id):
    for item in cart_items:
        if item['ProductId'] == product_id:
            cart_items.remove(item)
            break

    return "Product removed from cart!"


if __name__ == '__main__':
    app.run(debug=True)
