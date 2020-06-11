import os,csv

from flask import Flask, render_template, request
from models import Artist, Title, db

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://User:user@localhost/music'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

def main():
    f = open("artists.csv")
    reader = csv.reader(f)
    for artist_name in reader:
        artist= Artist(artist_name=artist_name)
        db.session.add(artist)
        print(f"Added artist {artist_name} into artist table.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
