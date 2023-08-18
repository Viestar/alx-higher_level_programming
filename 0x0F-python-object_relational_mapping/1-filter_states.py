#!/usr/bin/python3
""" Usage: ./0-select_states.py <username> <password> <database> """

from sys import argv
import sys
import MySQLdb as Qdb

if __name__ == "__main__":
    if len(argv) == 4:
        db = Qdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    else:
        sys.exit(1)
    curSor = db.cursor()
    curSor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    [print(state) for state in curSor.fetchall() if state[1][0] == "N"]
    curSor.close(), db.close()
