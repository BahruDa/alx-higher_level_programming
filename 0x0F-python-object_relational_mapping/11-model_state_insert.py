#!/usr/bin/python3
"""
a script that adds the State object
“Louisiana” to the database
"""

import sys
from model_state import Base, State
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))

    session.close()
