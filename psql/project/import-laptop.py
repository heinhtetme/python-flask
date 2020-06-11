import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql://User:user@localhost/project')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("laptop.csv")
    reader = csv.reader(f)
    for brand_name, type, price in reader:
        db.execute("insert into laptop (brand_name,type,price) values (:brand_name,:type,:price)",{"brand_name":brand_name,"type":type,"price":price})
        print(f"{type} {brand_name} cost {price}.")
    db.commit()

if __name__ == "__main__":
    main()
