#!/usr/bin/python3
""" Usage: ./0-select_states.py <username> <password> <database> <search> """

from sys import argv
import sys
import MySQLdb as Qdb

if __name__ == "__main__":
    if (len(argv) == 4):
        db = Qdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
        curSor = db.cursor()
        curSor.execute("SELECT `cities`.`id`, `cities`.`name`, \
                       `states`.`name` FROM `cities` INNER JOIN `states` \
        ON `cities`.`state_id` = `states`.`id` ORDER BY `cities`.`id` ASC")
        [print(city) for city in curSor.fetchall()], curSor.close(), db.close()
