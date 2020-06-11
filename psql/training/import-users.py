import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine(os.getenv("DATABASE_URL"))
engine = create_engine('postgresql://User:user@localhost/training')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("users.csv")
    reader = csv.reader(f)
    for user_name, course_id in reader:
        db.execute("INSERT INTO users (user_name, course_id) VALUES (:user_name, :course_id)",
                    {"user_name": user_name, "course_id": course_id})
        print(f"Added user {user_name} into users table.")
    db.commit()

if __name__ == "__main__":
    main()
