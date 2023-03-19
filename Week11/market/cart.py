import json

# Retrieve all products from products.json file
def retrieve_all_products():
    with open('products.json', 'r') as f:
        all_products = json.load(f)
    return all_products

# Add a product to the cart
def add_product_to_cart(product_id):
    with open('cart.json', 'r+') as f:
        cart_items = json.load(f)
        all_products = retrieve_all_products()
        for product in all_products:
            if product['ProductId'] == product_id:
                cart_items.append(product)
                break
        f.seek(0)
        json.dump(cart_items, f, indent=4)

# Remove a product from the cart
def remove_product_from_cart(product_id):
    with open('cart.json', 'r+') as f:
        cart_items = json.load(f)
        for product in cart_items:
            if product['ProductId'] == product_id:
                cart_items.remove(product)
                break
        f.seek(0)
        json.dump(cart_items, f, indent=4)
