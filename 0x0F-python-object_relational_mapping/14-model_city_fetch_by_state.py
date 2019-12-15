#!/usr/bin/python3
""" Write a Python file similar to model_state.py named model_city.py
that contains the class definition of a City.
"""
if __name__ == "__main__":
    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import asc, desc
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states_name = session.query(City, State)\
        .filter(State.id == City.state_id)\
        .order_by(asc(City.id)).all()
    for cities, states in states_name:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
    session.close()
