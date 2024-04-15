#!/usr/bin/python3

"""
contains the sqlalchemy code to
prints the first State object from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name.like("%n%"))\
        .order_by(State.id)

    for state in states:
        print(f'{state.id}: {state.name}')

    session.close()
