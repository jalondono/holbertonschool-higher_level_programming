#!/usr/bin/python3
""" prints the State object with the name passed as argument
    from the database hbtn_0e_6_usa
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
        .filter(State.name == sys.argv[4]). \
        order_by(State.id).all()

    if states_name:
        print("{}".format(states_name[0].id))
    else:
        print("Not found")
    session.close()
