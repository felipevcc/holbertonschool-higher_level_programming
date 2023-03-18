#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a'"""

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

    states_objs = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for stateObj in states_objs:
        print("{}: {}".format(stateObj.id, stateObj.name))

    session.close()
