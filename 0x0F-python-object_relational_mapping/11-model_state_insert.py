#!/usr/bin/python3
""" A script that uses sqlalchemy to list the first state.id """

from model_state import Base, State
from sys import argv
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) == 4:
        url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(state.id)
        session.close()
    else:
        sys.exit(1)
