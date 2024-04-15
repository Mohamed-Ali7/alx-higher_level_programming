#!/usr/bin/python3

"""
contains the class definition of a State and
an instance Base = declarative_base():
"""
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

Base = declarative_base()


class State(Base):

    """This class represent the states table in hbtn_0e_6_usa daatabase"""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
