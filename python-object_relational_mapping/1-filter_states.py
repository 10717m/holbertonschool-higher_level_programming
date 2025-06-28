#!/usr/bin/python3
"""
This script lists all states with starting with 'N' from database hbtn_0e_0_usa
It takes 3 arguments: MySQL username, password, and database name.
Connects to a MySQL server running on localhost at port 3306 using MySQLdb.
Results are sorted by states.id in ascending order.
"""

import MySQLdb
import sys


def main():
    """Connects to database and prints states with names starting with 'N'."""
    if len(sys.argv) != 4:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    # Query to select states where name starts with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print the results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Cleanup
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
