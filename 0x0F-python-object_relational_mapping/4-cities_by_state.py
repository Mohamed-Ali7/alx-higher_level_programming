#!/usr/bin/python3

"""
This module has a sql query to retrieve all cities
from the database hbtn_0e_4_usa
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

    cursor.execute("SELECT cities.id, cities.name, states.name FROM\
                   cities JOIN states ON cities.state_id=states.id\
                   ORDER BY cities.id")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
