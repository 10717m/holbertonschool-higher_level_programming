#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.
It takes 3 arguments: mysql username, mysql password, and database name.
It connects to localhost MySQL server at port 3306 using MySQLdb.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys


def main():
    """Main function to connect to database and print all states ordered by id."""
    if len(sys.argv) != 4:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost:3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cursor = db.cursor()

    # Execute SQL query to select all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results and print each row as a tuple
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Cleanup
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

