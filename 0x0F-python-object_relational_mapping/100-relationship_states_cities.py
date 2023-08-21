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
        city = City(name="San Fancisco", state=State(name="California"))
        session.add(city)
        session.commit()
        session.close()
    else:
        sys.exit(1)
