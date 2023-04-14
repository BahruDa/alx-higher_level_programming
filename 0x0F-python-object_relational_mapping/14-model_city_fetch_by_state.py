#!/usr/bin/python3
"""
a script that lists all State objects
from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    States = Base.classes.states
    session = Session(engine)

    states = (session.query(State, City).filter(City.state_id == State.id)
                     .order_by(City.id).all())
    for state, city in states:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
