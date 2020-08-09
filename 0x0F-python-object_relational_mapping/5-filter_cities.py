#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that
state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) < 5:
        exit()

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    num_rows = cur.execute("SELECT cities.name\
                           FROM cities LEFT JOIN states ON\
                           cities.state_id = states.id\
                           WHERE states.name LIKE BINARY %(state)s\
                           ORDER BY cities.id ASC", {'state': argv[4]})

    data = cur.fetchall()
    for i in range(num_rows):
        if i != num_rows - 1:
            print(data[i][0], end=', ')
        else:
            print(data[i][0])

    cur.close()
    db.close()
