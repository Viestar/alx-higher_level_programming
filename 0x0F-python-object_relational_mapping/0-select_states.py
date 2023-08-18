#!/usr/bin/python3
""" Usage: ./0-select_states.py <mysql username> <mysql password> <database name> """

from sys import argv
import sys
import MySQLdb as Qdb

if __name__ == "__main__":
	if len(argv) == 4:
		db = Qdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
	else:
		sys.exit(1)
	curSor = db.                             ()
	curSor.execute("SELECT * FROM `states` ORDER BY `id` ASC")
	[print(state) for state in curSor.fetchall()], curSor.close(), db.close()
		