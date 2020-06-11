import csv  
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://User:user@localhost/test')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("passengers.csv")
    reader = csv.reader(f)
    for name, flight_id in reader:
        db.execute("insert into passengers (name, flight_id) values (:name, :flight_id)", {"name":name, "flight_id":flight_id})
        print(f"{name} in {flight_id}")
    db.commit()

if __name__ == "__main__":
    main()