#!/usr/bin/python3

"""
list all states with a in their name
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    uname = sys.argv[1]
    psswd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(uname, psswd, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)

    for state in states:
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
