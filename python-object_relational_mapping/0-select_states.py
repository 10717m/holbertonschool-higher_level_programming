#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa in ascending order by id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract arguments
    username, password, db_name = sys.argv[1:4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()
