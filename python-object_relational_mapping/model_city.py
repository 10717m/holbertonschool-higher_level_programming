#!/usr/bin/python3
"""
Defines the City class and links to the MySQL table 'cities'.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        id (int): The city's id (primary key)
        name (str): The city's name
        state_id (int): The city's state id (foreign key)
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
