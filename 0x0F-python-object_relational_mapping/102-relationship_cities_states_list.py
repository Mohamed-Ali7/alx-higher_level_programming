#!/usr/bin/python3

"""
This module contains sqlalchemy code to that
lists all City objects from the database hbtn_0e_101_usa
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

    cities = session.query(City).order_by(City.id)

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
