from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Laptop(db.Model):
    __tablename__ = "laptops"
    id = db.Column(db.Integer,primary_key=True)
    brand = db.Column(db.String,nullable=False)
    type = db.Column(db.String,nullable=False)
    price = db.Column(db.Integer,nullable=False)
    customers = db.relationship("Customer",backref="laptop",lazy=True) 

    def add_customer(self,name):
        c = Customer(name=name,item_id=self.id)
        db.session.add(c)
        db.session.commit()

class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    item_id = db.Column(db.Integer,db.ForeignKey("laptops.id"),nullable=False)

class Saleperson(db.Model):
    __tablename__ = "saleperson"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    item_id = db.Column(db.Integer,db.ForeignKey("laptops.id"),nullable=False)
