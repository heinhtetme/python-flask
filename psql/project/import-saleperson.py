import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://User:user@localhost/project')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("saleperson.csv")
    reader = csv.reader(f)
    for sale_person, item_id in reader:
        db.execute("insert into saleperson (sale_person,item_id) values (:sale_person,:item_id)",{"sale_person":sale_person,"item_id":item_id})
        print(f"{sale_person} sold {item_id}")
    db.commit()

if __name__ == "__main__":
    main()