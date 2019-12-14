import MySQLdb
from sys import argv

size = len(argv) - 1
if size == 4:
    m_name = argv[1]
    m_passwd = argv[2]
    m_db = argv[3]
    db = MySQLdb.connect(host='localhost', user=m_name, passwd=m_passwd, db=m_db)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %(username)s ORDER BY id", {'username': argv[4]})
    rows = cur.fetchall()
    for data in rows:
        print(data)
