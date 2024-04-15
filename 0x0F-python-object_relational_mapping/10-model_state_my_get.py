#!/usr/bin/python3

"""
contains the sqlalchemy code to
prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter_by(name=state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
