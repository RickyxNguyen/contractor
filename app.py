from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

import os

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/KiWi')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()


products = db.products
products.drop()
carts = db.cart
carts.drop()

db.products.insert({"name":"WiBook Pro 15", "inventory":100, "description":"Authentic Chinese Knockoff of MacBook Pro 15", "image":"./static/matebook.png"})
db.products.insert({"name":"WiPro", "inventory":10, "description":"Authentic Chinese Knockoff of Mac Pro", "image":"./static/grater.png"})

app = Flask(__name__)


@app.route('/')
def show_products():
    """Show all playlists."""
    product = products.find()
    # This will display all playlists by looping through the database
    return render_template('products_show.html', products=product)

@app.route('/cart')
def show_cart():
    """Show all playlists."""
    cart = carts.find()
    # This will display all playlists by looping through the database
    return render_template('cart.html', carts=cart)



@app.route('/products/<product_id>/add', methods=['POST'])
def product_delete(product_id):
    # This will delete a playlist by using an id as a parameter
    """Delete one playlist."""
    if request.form.get('_method') == 'CREATE':
        carts.insert({'_id': ObjectId(product_id)})
        return redirect(url_for('show_cart'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
