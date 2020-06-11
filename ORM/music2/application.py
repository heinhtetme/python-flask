import os

from flask import Flask, render_template, request
from models import Artist, Title, db

app = Flask(__name__)

# engine = create_engine(os.getenv("DATABASE_URL"))
#engine = create_engine('postgresql://User:user@localhost/music')
#db = scoped_session(sessionmaker(bind=engine))

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://User:user@localhost/music'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)

@app.route("/")
def index():
    artists = Artist.query.all()
    return render_template("index.html", artists=artists)

@app.route("/playlist", methods=["POST"])
def playlist():
    """Track List."""

    # Get form information.
    artist_name = request.form.get("name")
    try:
        artist_id = int(request.form.get("artist_id"))
    except ValueError:
        return render_template("error.html", message="Invalid artist.")

    # Make sure artist exists.
    artist= Artist.query.get(artist_id)
    if artist is None:
        return render_template("error.html", message="No such artist with that id.")
    
    artist.add_title(name)
    return render_template("success.html")

@app.route("/artists")
def artists():
    """Lists all artists."""
    artists= Artist.query.all()
    return render_template("artists.html", artists=artists)

@app.route("/artist/<int:artist_id>")
def artist(artist_id):
    """Artist List."""

    # Make sure course exists.
    artist=Artist.query.get(artist_id)
    if artist is None:
        return render_template("error.html", message="No such artist.")

    # Get all titles.
    titles = artist.titles
    return render_template("artist.html", artist=artist, titles=titles)

    
if __name__ == '__main__':
    app.run(debug=True)