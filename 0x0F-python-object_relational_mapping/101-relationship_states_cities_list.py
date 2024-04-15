#!/usr/bin/python3

"""
This module contains sqlalchemy code to that lists all State objects,
and corresponding City objects, contained in the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    query = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(State.id, City.id).all()

    current_state = None
    for state, city in query:
        if state != current_state:
            print(f"{state.id}: {state.name}")
            current_state = state
        print(f"    {city.id}: {city.name}")

    session.close()
