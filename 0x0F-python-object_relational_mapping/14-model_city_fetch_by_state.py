#!/usr/bin/python3

"""
contains the sqlalchemy code to
prints all City objects from the database hbtn_0e_14_usa:
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(State.name, City.id, City.name).join(State)\
        .order_by(City.id)

    for city in cities:
        print(f"{city[0]}: ({city[1]}) {city[2]}")
    session.close()
