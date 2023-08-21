#!/usr/bin/python3
# Lists all City objects from the database hbtn_0e_101_usa.
""" Script uses relation  """
import sys
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        engine = create_engine("mysql+mysqldb://{}:{} \
                        @localhost/{}".format(argv[1], argv[2], argv[3]),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        [print(f"{city[0]}: {city[1]} -> {city[2]}")
            for city in session.query(City).order_by(City.id)]
    else:
        sys.exit(1)
