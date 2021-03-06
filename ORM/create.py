from flask import Flask, render_template, request
from models import Flight, Passenger,db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://User:user@localhost/orm"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()