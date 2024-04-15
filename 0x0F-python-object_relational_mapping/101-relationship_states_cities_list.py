#!/usr/bin/python3

"""
This module contains sqlalchemy code to that lists all State objects,
and corresponding City objects, contained in the database hbtn_0e_101_usa
"""

if __name__ == "__main__":

    """This code doesn't execute if the file is imported"""

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State
    from relationship_city import City

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
