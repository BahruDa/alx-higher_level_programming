#!/usr/bin/python3
"""
<<<<<<< HEAD
a script that deletes all State objects with a
name containing the letter a from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import delete


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Base = automap_base()
    Base.prepare(engine, reflect=True)

    States = Base.classes.states
    session = Session(engine)

    delete_state = (delete(State).where(State.name.contains('a')))
    session.execute(delete_state)
    session.commit()

    session.close()
=======
delete all State object
with a name containing the letter `a`
from the db.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects on the db.
    """

    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    eng = create_engine(db_uri)
    Session = sessionmaker(bind=eng)

    ses = Session()

    for instance in ses.query(State).filter(State.name.contains('a')):
        ses.delete(instance)

    ses.commit()
    ses.close()
>>>>>>> 3274e97c5c5550971d27fcf8b73e6f78feb0abff
