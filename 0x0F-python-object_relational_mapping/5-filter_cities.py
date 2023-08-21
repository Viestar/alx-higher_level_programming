#!/usr/bin/python3
""" script that lists all cities of a given state """

import MySQLdb as Qdb
import sys
from sys import argv

if __name__ == "__main__":
    if len(argv) == 5:
        ur = argv[1]
        pd = argv[2]
        de = argv[3]
        se = argv[4]
        cs = []
        db = Qdb.connect(host="localhost", port=3306,
                         user=ur, passwd=pd, db=de)
        curSor = db.cursor()
        curSor.execute("""SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states ON cities.state_id = states.id
            WHERE states.name=%s
            ORDER BY id ASC""", (se,))
        rows = curSor.fetchall()
        for row in rows:
            cs.append(row[1])
            print(', '.join(row))
            curSor.close()
            db.close()
    else:
        sys.exit(1)
