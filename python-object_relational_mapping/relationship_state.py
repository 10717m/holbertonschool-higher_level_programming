#!/usr/bin/python3
"""
Defines the State class with relationship to City.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City

Base = declarative_base()

class State(Base):
    """
    Represents a state for a MySQL database with relationship to City.
    
    Attributes:
        id (int): The state's id (primary key)
        name (str): The state's name
        cities (relationship): Relationship to City objects (cascade delete)
    """
    __tablename__ = 'states'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
