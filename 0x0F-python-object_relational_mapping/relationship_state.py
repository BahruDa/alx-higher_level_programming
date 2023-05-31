#!/usr/bin/python3
"""
a python module that contains the class definition of
a State and a relationship state
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''
    defines a state
    Attr:
    id (int): auto-generated, unique integer, not null, & is a primary key
    name (): a column of a string with 128 chars and can’t be null
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City", cascade='delete', backref="state"
    )
