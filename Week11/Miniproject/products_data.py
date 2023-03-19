import json

def retrieve_all_products():
    with open("products.json", "r") as f:
        all_products = json.load(f)
    return all_products

def retrieve_requested_product(product_id):
    with open("products.json", "r") as f:
        all_products = json.load(f)
    for product in all_products:
        if product["id"] == product_id:
            return product
    return None
