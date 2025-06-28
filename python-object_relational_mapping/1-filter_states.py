#!/usr/bin/python3
"""
Lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa, sorted by states.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username, password, db_name = sys.argv[1:4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # SQL query to filter states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and print all results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cursor.close()
    db.close()
