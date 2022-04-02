#!/usr/bin/python3
"""
list all cities

"""

import MySQLdb
import sys

if __name__ == "__main__":
    user_n = sys.argv[1]
    pass_w = sys.argv[2]
    data_b = sys.argv[3]
    db = MySQLdb.connect(user=user_n, passwd=pass_w, db=data_b)
    cur = db.cursor()
    cur.execute("SELECT c.id,c.name, s.name \
    FROM `cities`AS c \
    INNER JOIN `states` AS s \
    ON c.state_id = s.id \
    ORDER BY c.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
