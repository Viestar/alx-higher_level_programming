#!/usr/bin/python3
""" A script that deletes all State objects with a name containing the
letter "a" from the database hbtn_0e_6_usa."""

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

        for state in session.query(State).all():
            if "a" in state.name:
                session.delete(state)
        session.commit()
        session.close()
    else:
        sys.exit(1)
