#!/usr/bin/python3
"""Lists the first State object"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    stateObj = session.query(State).order_by(State.id).first()
    if stateObj:
        print("{}: {}".format(stateObj.id, stateObj.name))
    else:
        print("Nothing")

    session.close()
