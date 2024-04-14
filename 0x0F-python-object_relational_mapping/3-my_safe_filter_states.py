#!/usr/bin/python3

"""
This module has a sql query to retrieve all states
where state name equals a specific valule
from hbtn_0d_usa database using MySQLdb module
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_to_search = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name= BINARY %s",
                   (state_to_search,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
