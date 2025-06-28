#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        sys.exit(1)

    # Get connection parameters and state name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create database connection
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query state by name (SQL injection free)
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
