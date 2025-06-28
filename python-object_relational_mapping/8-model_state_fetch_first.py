#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get connection parameters from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Create a configured Session class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()
