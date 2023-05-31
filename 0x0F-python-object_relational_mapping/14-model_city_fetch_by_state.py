#!/usr/bin/python3
"""
<<<<<<< HEAD
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
=======
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Session = sessionmaker(bind=eng)

    ses = Session()

    query = ses.query(City, State).join(State)

    for _c, _s in query.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))

    ses.commit()
    ses.close()
>>>>>>> 3274e97c5c5550971d27fcf8b73e6f78feb0abff
