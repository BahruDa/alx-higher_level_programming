#!/usr/bin/python3
"""
a python module that contains the class definition
of a City. and a relationship status"
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base, State


class City(Base):
    '''
    defines a state
    Attr:
    id (int): auto-generated, unique integer, not null, & is a primary key
    name (): a column of a string with 128 chars and can’t be null
    state_id (int): column of an integer, can’t be null and is a foreign key
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
