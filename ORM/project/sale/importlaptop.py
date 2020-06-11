import csv
from flask import Flask, render_template, request
from models import Laptop, db    

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://User:user@localhost/orm"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("laptop.csv")
    reader = csv.reader(f)
    for brand, type, price in reader:
        laptop = Laptop(brand=brand, type=type, price=price)
        db.session.add(laptop)
        print(f"{brand}, {type}, {price}")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
