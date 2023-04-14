#!/usr/bin/python3
"""
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
