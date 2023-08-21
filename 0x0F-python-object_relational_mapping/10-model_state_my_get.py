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
        right_state = [state for state in session.query(State)
                       .filter_by(name=param).first()]
        if right_state is not None:
            print(right_state.id)
        else:
            print("Not found")
        session.close()
    else:
        sys.exit()
