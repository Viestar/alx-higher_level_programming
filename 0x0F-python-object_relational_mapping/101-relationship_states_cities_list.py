#!/usr/bin/python3

""" A Script that retrive States objects and corresponding city objects """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
import sys
from relationship_state import State
from sqlalchemy.sql import select

if __name__ == "__main__":
    if len(argv) == 4:
        url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()
        result = select([City.id, City.name, State.name]).join(
            State, City.state_id == State.id).order_by(City.id)
        states_cities = session.execute(result)

        current_state = None
        for state, city in states_cities:
            if state != current_state:
                print(f"{state.id}: {state.name}")
                current_state = state
            print(f"\t{city.id}: {city.name}")

        # Close the session
        session.close()
    else:
        sys.exit(1)
