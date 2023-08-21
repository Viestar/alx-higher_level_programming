#!/usr/bin/python3
""" script that lists all cities of a given state """

import MySQLdb as Qdb
import sys
from sys import argv


if __name__ == "__main__":
    if len(argv) == 5:
        db = Qdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
        curSor = db.cursor()
        params = argv[4]
        curSor.execute("""SELECT cities.id, cities.name, states.name
            FROM cities INNER JOIN states ON cities.state_id = states.id
            WHERE states.name=%s
            ORDER BY id ASC""", (params,))
        [print(", ".join(city[1])) for city in curSor.fetchall()]
        curSor.cloe(), db.close()
    else:
        sys.exit(1)
