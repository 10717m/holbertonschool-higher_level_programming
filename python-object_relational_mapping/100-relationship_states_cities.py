#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco".
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

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

    # Create all tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create California with San Francisco
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close session
    session.close()
