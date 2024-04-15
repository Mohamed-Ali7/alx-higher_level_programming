#!/usr/bin/python3

"""
This module contains sqlalchemy code to that lists all State objects,
and corresponding City objects, contained in the database hbtn_0e_101_usa
"""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State, Base

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
