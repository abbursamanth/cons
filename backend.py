from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    { 'id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 999.99 },
    { 'id': 2, 'name': 'Smartphone', 'category': 'Electronics', 'price': 699.99 },
    { 'id': 3, 'name': 'Shampoo', 'category': 'Beauty', 'price': 9.99 },
    { 'id': 4, 'name': 'Conditioner', 'category': 'Beauty','price': 9.90},
    { 'id': 5, 'name': 'Toothpaste', 'category': 'beauty','price' : 5.0},
    {'id': 6, 'name': 'Pant', 'category': 'fashion','price' : 25.0},
    
]

orders = []

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/orders', methods=['POST'])
def add_order():
    order = request.json
    orders.append(order)
    return jsonify(order), 201

@app.route('/api/analysis', methods=['GET'])
def get_analysis():
    total_revenue = sum(order['total'] for order in orders)
    total_orders = len(orders)
    average_order_value = total_revenue / total_orders if total_orders > 0 else 0

    analysis = {
        'totalRevenue': total_revenue,
        'totalOrders': total_orders,
        'averageOrderValue': average_order_value,
        'highestSellingProduct': 'Laptop',  # Placeholder value
        'highestProfitMakingProduct': 'Smartphone',  # Placeholder value
        'mostLikedProduct': 'Shampoo'  # Placeholder value
    }
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True)
