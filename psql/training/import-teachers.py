import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine('postgresql://User:user@localhost/training')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("teachers.csv")
    reader = csv.reader(f)
    for teacher_name, course_id in reader:
        db.execute("INSERT INTO teachers (teacher_name, course_id) VALUES (:teacher_name, :course_id)",
                    {"teacher_name": teacher_name, "course_id": course_id})
        print(f"Added teacher {teacher_name} into teachers table.")
    db.commit()

if __name__ == "__main__":
    main()
