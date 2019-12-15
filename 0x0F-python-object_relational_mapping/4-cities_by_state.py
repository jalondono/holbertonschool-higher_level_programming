#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

if __name__ == "__main__":
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
    cur.execute("SELECT B.id, B.name, A.name "
                "FROM states A JOIN cities B ON A.id = B.state_id "
                "ORDER BY B.id")
    rows = cur.fetchall()
    for data in rows:
        print(data)
    cur.close()
    db.close()
