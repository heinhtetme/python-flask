from flask import Flask, render_template, request
from models import Laptop, Customer, Saleperson, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://User:user@localhost/orm"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    laptops = Laptop.query.all()
    return render_template("index.html",laptops=laptops)

@app.route("/order", methods=["POST"])
def order():
    """Order a Laptop"""
    name = request.form.get("name")
    try:
        item_id = int(request.form.get("item_id"))
    except ValueError:
        return render_template("error.html",message="Invalid item number.")
    laptop = Laptop.query.get(item_id)
    if not laptop:
        return render_template("error.html",message="No such item with that id.")
    
    laptop.add_customer(name)
    return render_template("success.html")

@app.route("/laptops")
def laptops():
    """List all laptops."""
    laptops = Laptop.query.all()
    return render_template("laptops.html",laptops=laptops)

@app.route("/laptops/<int:item_id>")
def laptop(item_id):
    """List details about a sigle laptop"""
    laptop = Laptop.query.get(item_id)
    if laptop is None:
        return render_template("error.html",message="No such item.")
    
    customers = laptop.customers
    return render_template("laptop.html",laptop=laptop,customers=customers)

if __name__ == "__main__":
    app.run(debug=1)