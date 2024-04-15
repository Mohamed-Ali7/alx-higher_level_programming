#!/usr/bin/python3

"""contains the class definition of a City and"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):

    """This class represent the cities table in hbtn_0e_6_usa daatabase"""

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
