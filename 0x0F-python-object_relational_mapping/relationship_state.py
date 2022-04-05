#!/usr/bin/python3

"""
this module comtains the state class
"""

from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer, ForeignKey, String
from relationship_city import Base


class State(Base):
    """
    represents the states table
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
