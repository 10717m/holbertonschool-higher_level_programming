#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
and displays them with their corresponding state name.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get credentials and DB name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Query to join cities and states and sort by cities.id
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(query)

    # Print the result rows
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
