#!/usr/bin/python3
"""
Defines the City class with relationship to State.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """
    Represents a city for a MySQL database with relationship to State.
    
    Attributes:
        id (int): The city's id (primary key)
        name (str): The city's name
        state_id (int): The city's state id (foreign key)
    """
    __tablename__ = 'cities'
    
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
