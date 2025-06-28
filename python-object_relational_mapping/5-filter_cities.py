#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Safe from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Parse command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor
    cursor = db.cursor()

    # Parameterized query to avoid SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()

    # Print as comma-separated string
    print(", ".join([city[0] for city in cities]))

    # Cleanup
    cursor.close()
    db.close()
