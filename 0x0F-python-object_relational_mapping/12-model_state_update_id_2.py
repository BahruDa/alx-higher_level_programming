#!/usr/bin/python3
"""
a script that changes the name of a State
object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import update


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    States = Base.classes.states
    session = Session(engine)

    update_state = (update(State).values(name='New Mexico')
                    .where(State.id == 2))
    session.execute(update_state)
    session.commit()

    session.close()
