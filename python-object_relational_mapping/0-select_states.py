#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: MySQL username, MySQL password, and database name.
It connects to a MySQL server running on localhost at port 3306 using MySQLdb.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


def main():
    """Connect to database and list all states sorted by id in ascending order."""
    if len(sys.argv) != 4:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

