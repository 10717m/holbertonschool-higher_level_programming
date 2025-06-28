#!/usr/bin/python3
"""
Script that changes the name of the State object with id=2 to 'New Mexico'
in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(
            sys.argv[0]))
        sys.exit(1)

    # Get connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the state with id=2
    state = session.query(State).filter(State.id == 2).first()

    # Update the state name if found
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
