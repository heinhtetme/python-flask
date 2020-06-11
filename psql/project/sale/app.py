from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://User:user@localhost/project")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    laptops = db.execute("select * from laptop").fetchall()
    return render_template("index.html",laptops=laptops)

@app.route("/order", methods=["POST"])
def order():
    """Order a Laptop"""
    name = request.form.get("name")
    try:
        item_id = int(request.form.get("item_id"))
    except ValueError:
        return render_template("error.html",message="Invalid item number.")
    if db.execute("select * from laptop where id=:id",{"id":item_id}).rowcount==0:
        return render_template("error.html",message="No such item with that id.")
    db.commit()
    return render_template("success.html")

@app.route("/laptops")
def laptops():
    """List all laptops."""
    laptops = db.execute("select * from laptop").fetchall()
    return render_template("laptops.html",laptops=laptops)

@app.route("/laptops/<int:item_id>")
def laptop(item_id):
    """List details about a sigle laptop"""
    laptop = db.execute("select * from laptop where id=:id",{"id":item_id}).fetchone()
    if laptop is None:
        return render_template("error.html",message="No such item.")
    customers = db.execute("select customer_name from customer where item_id = :item_id",{"item_id":item_id}).fetchall()
    return render_template("laptop.html",laptop=laptop,customers=customers)

if __name__ == "__main__":
    app.run(debug=1)