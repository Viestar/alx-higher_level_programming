#!/usr/bin/python3
""" Script that creates a new state """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from relationship_city import City, Base
from relationship_state import State
import sys


if __name__ == "__main__":
    if len(argv) == 4:
        url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
        engine = create_engine(url)
        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()
        new_state = State(name="California")
        new_city = City(name="San Francisco")
        new_state.cities.append(new_city)

        session.add(new_state)

        session.commit()
        session.close()
    else:
        sys.exit(1)
