#!/usr/bin/python3

"""
contains the class definition of a State and
an instance Base = declarative_base():
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):

    """This class represent the states table in hbtn_0e_6_usa daatabase"""

    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state",
                          cascade="all, delete")
