#!/usr/bin/python3

"""
This module has a sql query to lists all cities of a state,
from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    cursor.execute("SELECT name FROM\
                   cities where state_id=\
                   (SELECT id from states where name=%s)\
                   ORDER BY id", (state_name,))

    cities = [row[0] for row in cursor.fetchall()]

    print(", ".join(cities))
    cursor.close()
    db.close()
