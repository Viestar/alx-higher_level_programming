#!/usr/bin/python3

""" A Script that retrive States objects and corresponding city objects """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City
from relationship_state import State
import sys

if __name__ == "__main__":
    if len(argv) == 4:
        url = "mysql+mysqldb://%s:%s@localhost/%s"
        params = (argv[1], argv[2], argv[3])
        engine = create_engine(url, params)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        [print(f"{state.id}: {state.name}\n \t{city.id}: {city.name}")
            for state, city in session.query(City, State)], session.close()
    else:
        sys.exit(1)
