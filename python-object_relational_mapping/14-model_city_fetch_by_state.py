#!/usr/bin/python3
"""Lists all City objects"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities_objs = session.query(City).order_by(City.id).all()

    for cityObj in cities_objs:
        print("{}: ({}) {}".format(
            cityObj.state.name, cityObj.id, cityObj.name))

    session.close()
