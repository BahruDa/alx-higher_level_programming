#!/usr/bin/python3
"""
a script that creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    States = Base.classes.states
    session = Session(engine)

    california = State(name='California')
    sanfrancisco = City(name='San Francisco')
    california.cities.append(sanfrancisco)
    session.add(sanfrancisco)
    session.commit()

    session.close()
