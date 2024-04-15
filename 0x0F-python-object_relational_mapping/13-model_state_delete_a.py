#!/usr/bin/python3

"""changes the name of a State object from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database), echo=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states_to_delete = session.query(State).filter(State.name.like("%a%"))

    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
