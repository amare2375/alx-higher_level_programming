#!/usr/bin/python3
"""
    A script that changes teh name of a State object in hbtn_0e_6_usa
    name of State where id = 2 to New Mexico
    Username, password, dbname will be passed as arguments to the script.
"""

import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    q = session.query(State).filter(State.id == 2).first()
    q.name = 'New Mexico'
    session.commit()
    session.close()
