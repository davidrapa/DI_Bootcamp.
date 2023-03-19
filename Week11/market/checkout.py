import json

# Retrieve all cart items from cart.json file
def retrieve_cart_items():
    with open('cart.json', 'r') as f:
        cart_items = json.load(f)
    return cart_items

# Calculate total price of all cart items
def calculate_total_price(cart_items):
    total_price = 0
    for item in cart_items:
        total_price += item['Price']
    return total_price

if __name__ == '__main__':
    cart_items = retrieve_cart_items()
    total_price = calculate_total_price(cart_items)
    print(f'Cart items: {cart_items}')
    print(f'Total price: {total_price}')
