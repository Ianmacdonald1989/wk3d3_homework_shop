from flask import render_template
from app import app 
from models.list_orders import orders 

@app.route('/orders')
def show_orders():
    return render_template("index.html", orders_list=orders)

@app.route('/orders/<index>')
def show_order(index):
    index = int(index)
    order = orders[index]
    return render_template("order.html", order=order)