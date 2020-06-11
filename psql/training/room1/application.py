import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine('postgresql://User:user@localhost/training')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    courses = db.execute("SELECT * FROM courses").fetchall()
    return render_template("index.html", courses=courses)

@app.route("/enroll", methods=["POST"])
def enroll():
    """Enrollments."""

    # Get form information.
    user_name = request.form.get("name")
    try:
        course_id = int(request.form.get("course_id"))
    except ValueError:
        return render_template("error.html", message="Invalid class.")

    # Make sure flight exists.
    if db.execute("SELECT * FROM courses WHERE id = :id", {"id": course_id}).rowcount == 0:
        return render_template("error.html", message="No such course with that id.")
    db.execute("INSERT INTO users (user_name, course_id) VALUES (:user_name, :course_id)",
            {"user_name": user_name, "course_id": course_id})
    db.commit()
    return render_template("success.html")

@app.route("/courses")
def courses():
    """Lists all courses."""
    courses = db.execute("SELECT * FROM courses").fetchall()
    return render_template("courses.html", courses=courses)

@app.route("/courses/<int:course_id>")
def course(course_id):
    """Lists details about a particular course."""

    # Make sure course exists.
    course = db.execute("SELECT * FROM courses WHERE id = :id", {"id": course_id}).fetchone()
    if course is None:
        return render_template("error.html", message="No such class.")

    # Get all users.
    users = db.execute("SELECT user_name FROM users WHERE course_id = :course_id",
                            {"course_id": course_id}).fetchall()

    # Get teachers
    teachers = db.execute("SELECT teacher_name FROM teachers WHERE course_id = :course_id",
                            {"course_id": course_id}).fetchall()
    return render_template("course.html", course=course, users=users, teachers=teachers)

    
if __name__ == '__main__':
    app.run(debug=True)