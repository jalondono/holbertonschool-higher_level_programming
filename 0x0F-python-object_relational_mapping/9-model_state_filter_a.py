#!/usr/bin/python3
""" lists all State objects that contain the letter a
    from the database
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import asc, desc
    from model_state import Base, State
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states_name = session.query(State)\
        .filter(State.name.contains('a'))\
        .order_by(asc(State.id))
    for idx, name in enumerate(states_name):
        print("{:d}: {}".format(name.id, name.name))
    session.close()
