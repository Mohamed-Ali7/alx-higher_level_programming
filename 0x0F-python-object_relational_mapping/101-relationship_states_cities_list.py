#!/usr/bin/python3
"""This module contains sqlalchemy code to that lists all State objects,
and corresponding City objects, contained in the database hbtn_0e_101_usa"""

if __name__ == "__main__":

    import sys
    from relationship_city import City
    from relationship_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
