import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine('postgresql://User:user@localhost/training')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("courses.csv")
    reader = csv.reader(f)
    for course_name, section in reader:
        db.execute("INSERT INTO courses (course_name, section) VALUES (:course_name, :section)",
                    {"course_name": course_name, "section": section})
        print(f"Added course name {course_name} and section {section} into courses table.")
    db.commit()

if __name__ == "__main__":
    main()
