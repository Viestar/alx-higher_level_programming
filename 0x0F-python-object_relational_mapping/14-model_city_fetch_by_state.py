#!/usr/bin/python3
""" A script that lists all State objects via SQLAlchemy """

import sys
from sys import argv
from sqlalchemy import create_engine
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(argv) == 4:
        url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
        engine = create_engine(url, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        [print(f"{state.name}: ({city.id}) {city.name}") for state, city in
            session.query(State, City).filter(City.state_id == State.id)
            .all()].order_by(City.id), session.close()
    else:
        sys.exit(1)
