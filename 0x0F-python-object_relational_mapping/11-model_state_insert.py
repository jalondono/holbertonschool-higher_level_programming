#!/usr/bin/python3
""" adds the State object “Louisiana”
to the database hbtn_0e_6_usa
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
    Louisiana = State(name="San pedro")
    session.add(Louisiana)
    session.commit()
    print(Louisiana.id)
    session.close()
