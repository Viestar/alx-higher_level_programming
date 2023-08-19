#!/usr/bin/python3
""" A script that lists all State objects via SQLAlchemy """

import sys
from sys import argv
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(argv) == 4:
        engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@'localhost/{argv[3]}'")
        Session = sessionmaker()
        session = Session()
        [print(f"{state.id}: {state.name}") for state in
            session.query(State).order_by(State.id)]
    else:
        sys.exit(1)
