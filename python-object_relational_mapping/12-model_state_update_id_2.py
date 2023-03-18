#!/usr/bin/python3
"""Updates the name on a State object"""

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

    stateObj = session.query(State).filter_by(id=2).first()
    stateObj.name = "New Mexico"
    session.commit()

    states_objs = session.query(State).order_by(State.id).all()
    for stateObj in states_objs:
        print("{}: {}".format(stateObj.id, stateObj.name))

    session.close()
