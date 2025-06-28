#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
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

    # Query all cities with their states, ordered by city id
    cities = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id)\
        .all()

    # Display results in required format
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
