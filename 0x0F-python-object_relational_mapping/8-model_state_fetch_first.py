#!/usr/bin/python3

"""
print the first state object

"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(uname, passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).first()

    print("{}: {}".format(state.id, state.name))
