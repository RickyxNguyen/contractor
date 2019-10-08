from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from random import randint
host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/KiWi')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()


products = db.products
products.drop()
carts = db.carts
carts.drop()

db.products.insert_many([{"name":"WiBook Pro 15", "description":"Authentic Chinese Knockoff of MacBook Pro 15","price":3000, "image":"./static/matebook.png"},
                        {"name":"WiPro", "description":"Authentic Chinese Knockoff of Mac Pro","price":10000, "image":"./static/grater.png"}])

app = Flask(__name__)


@app.route('/')
def show_products():
    """Show all products."""
    product = products.find()
    # This will display all products by looping through the database
    return render_template('products_show.html', products=product)

@app.route('/cart')
def show_cart():
    """Show cart."""
    cart = carts.find()
    # This will display all products by looping through the database
    return render_template('cart.html', carts=cart)



@app.route('/products/<product_id>/add', methods=['POST'])
def product_create(product_id):
    # This will delete a product by using an id as a parameter
    """Add one product to cart"""


    product = products.find_one({'_id':ObjectId(product_id)})

    carts.insert(product)
        
    return redirect(url_for('show_cart'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
