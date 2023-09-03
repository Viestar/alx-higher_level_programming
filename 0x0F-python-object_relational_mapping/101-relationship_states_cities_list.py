#!/usr/bin/python3

""" A Script that retrive States objects and corresponding city objects """
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
from sqlalchemy.sql import select

if __name__ == "__main__":
    url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = select([City.id, City.name, State.name]).join(
        State, City.state_id == State.id).order_by(City.id)
    states_cities = session.execute(result)

    # for state in session.query(State).order_by(State.id):
    #     print("{}: {}".format(state.id, state.name))
    #     for city in state.cities:
    #         print("\t{}: {}".format(city.id, city.name))

    current_state = None
    for state in states_cities:
        print(f"{state.id}: {state.name}")
        for city in states_cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()
