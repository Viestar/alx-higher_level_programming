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
        url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        [print(f"{state.id}: {state.name}\n\t{city.id}: {city.name}")
            for state in session.query(City).order_by(State.id)
            for city in session.query(State).order_by(City.id)]
        session.close()
    else:
        sys.exit(1)
