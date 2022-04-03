#!/usr/bin/python3

"""
delete all states with 'a' in their name
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(uname, passwd, db)
    )

    session = sessionmaker(bind=engine)()

    states = session.query(State)

    for state in states:
        if "a" in state.name:
            session.delete(state)

    session.commit()
