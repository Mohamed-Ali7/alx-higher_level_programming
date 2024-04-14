#!/usr/bin/python3

"""
This module has a sql query to retrieve all states
with name starts with N letter from hbtn_0d_usa database using MySQLdb module
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s", ("N%",))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
