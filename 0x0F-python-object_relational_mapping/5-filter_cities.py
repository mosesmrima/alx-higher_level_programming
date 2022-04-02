#!/usr/bin/python3
"""
list all cities in a particular state

"""

import MySQLdb
import sys

if __name__ == "__main__":
    user_n = sys.argv[1]
    pass_w = sys.argv[2]
    data_b = sys.argv[3]
    state_n = sys.argv[4]
    db = MySQLdb.connect(user=user_n, passwd=pass_w, db=data_b)
    cur = db.cursor()

    cur.execute("SELECT * FROM `cities` AS `c` \
    INNER JOIN `states` AS `s` \
    ON `c`.`state_id` = `s`.`id` \
    ORDER BY `c`.`id`")

    rows = cur.fetchall()
    print(", ".join([row[2] for row in rows if row[4] == state_n]))
