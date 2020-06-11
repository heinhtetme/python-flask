from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
db=SQLAlchemy()

class Artist(db.Model):
    __tablename__='artists'
    id=db.Column(db.Integer,primary_key=True)
    artist_name=db.Column(db.String,nullable=False)
    titles=db.relationship("Title", backref="artists",lazy=True)
    
    def add_title(self,name):
        title=Title(name=name, artist_id=self.id)
        db.session.add(title)
        db.session.commit()


class Title(db.Model):
    __tablename__='titles'
    id=db.Column(db.Integer,primary_key=True)
    title_name=db.Column(db.String,nullable=False)
    artist_id=db.Column(db.Integer,db.ForeignKey('artists.id'),nullable=False)