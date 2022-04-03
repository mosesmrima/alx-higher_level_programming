#!/usr/bin/python3

"""
update a state name, given state id
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(uname, passwd, db)
    )

    session = sessionmaker(bind=engine)()

    state = session.query(State).filter(State.id == 2).first()

    state.name = "New Mexico"
    session.commit()
