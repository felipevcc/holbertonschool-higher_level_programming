#!/usr/bin/python3
"""Adds a new State object"""

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

    newRecord = State(name="Louisiana")
    session.add(newRecord)
    session.commit()

    stateObj = session.query(State).order_by(State.id.desc()).first()

    print(stateObj.id)

    session.close()
