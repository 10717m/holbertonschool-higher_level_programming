#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument passed as the 4th argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Read arguments
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor and execute query using string formatting
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Print all matching rows
    for row in cursor.fetchall():
        print(row)

    # Close resources
    cursor.close()
    db.close()
