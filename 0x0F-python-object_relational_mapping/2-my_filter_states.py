#!/usr/bin/python3
"""
takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

m_name = argv[1]
m_passwd = argv[2]
m_db = argv[3]
db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user=m_name,
                     passwd=m_passwd,
                     db=m_db)
cur = db.cursor()
cur.execute("SELECT * FROM states "
            "WHERE name LIKE '{:s}' "
            "ORDER BY states.id".format(argv[4]))
rows = cur.fetchall()
for data in rows:
    print(data)
cur.close()
db.close()
