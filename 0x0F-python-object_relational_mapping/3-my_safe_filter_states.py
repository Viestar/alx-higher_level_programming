#!/usr/bin/python3
""" Usage: ./0-select_states.py <username> <password> <database> <search> """

from sys import argv
import sys
import MySQLdb as Qdb

if __name__ == "__main__":
    if len(argv) == 5:
        db = Qdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
        curSor = db.cursor()
        query = "SELECT * FROM `states` WHERE `name`='{}' ORDER BY `id` ASC"
        params = argv[4]
        curSor.execute(query, (params,))
        [print(state) for state in curSor.fetchall() if state[1] == argv[4]]
        curSor.close(), db.close()
    else:
        sys.exit(1)
