#!/usr/bin/python3
""" script that lists all cities of a given state """

import MySQLdb as Qdb
import sys
from sys import argv


if __name__ == "__main__":
    db = Qdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"
    param = argv[4]
    cursor.execute(query, (param,))
    city_rows = cursor.fetchall()

    cities = [city[1] for city in city_rows]
    formated_city_name = ", ".join(cities)
    print(formated_city_name)
    cursor.close()
    db.close()
