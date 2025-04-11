from flask import Flask, request, jsonify
from cart import ShoppingCart

app = Flask(__name__)
cart = ShoppingCart()

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    cart.add_item(data['item'], data['quantity'])
    return jsonify({"status": "added"})

@app.route('/remove', methods=['DELETE']) 
def remove():
    data = request.json
    cart.remove_item(data['item'], data['quantity'])
    return jsonify({"status": "removed"})

@app.route('/total', methods=['GET'])
def total():
    return jsonify({"total": cart.get_total_items()})

if __name__ == '__main__':
    app.run()