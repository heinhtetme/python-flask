import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://User:user@localhost/project")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("customer.csv")
    reader = csv.reader(f)
    for customer_name, item_id in reader:
        db.execute("insert into customer (customer_name,item_id) values (:customer_name,:item_id)",{"customer_name":customer_name,"item_id":item_id})
        print(f"{customer_name} bought {item_id}.")
    db.commit()

if __name__ == "__main__":
    main()