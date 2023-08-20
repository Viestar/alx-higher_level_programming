#!/usr/bin/python3
""" script that lists all cities of a given state """

import MySQLdb as Qdb
import sys
from sys import argv

if __name__ == "__main__":
    if len(argv) == 4:
        db = Qdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
        curSor = db.cursor()
        query = "SELECT * FROM cities INNER JOIN states ON \
        WHERE cities.state_id = state.id ORDER BY cities.id ASC"
        params = argv[4]
        curSor.execute(query)
        [print(", ".join(city[2])) for city in
            curSor.fetchall() if city == params]
        curSor.cloe(), db.close()
    else:
        sys.exit(1)
