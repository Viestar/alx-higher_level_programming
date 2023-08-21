#!/usr/bin/python3
""" A SQL injection free script that prints the id of a given state. """

import sys
from sys import argv
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(argv) == 5:
        param = argv[4]
        url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
        engine = create_engine(url)

        Session = sessionmaker(bind=engine)

        session = Session(engine)
        state = session.query(State).filter(State.name == param).first()

        if state:
            print("{}".format(state.id))
        else:
            print("Not found")

        session.close()
    else:
        sys.exit(1)
