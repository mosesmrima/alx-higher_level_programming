#!/usr/bin/python3

"""
list states from the db using a specified name
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user_n = sys.argv[1]
    pass_w = sys.argv[2]
    data_b = sys.argv[3]
    host_n = "localhost"
    db = MySQLdb.connect(host=host_n, user=user_n, passwd=pass_w, db=data_b)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
