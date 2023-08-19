#!/usr/bin/python3
""" A SQL injection free script that prints the id of a given state. """

import sys
from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(argv) == 5:
        url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()
        param = argv[4]
        state = session.query(State).filter(State.name == param)
        if state is not None:
            print(state.id)
        else:
            print("Not found")
        session.close()
    else:
        sys.exit()
