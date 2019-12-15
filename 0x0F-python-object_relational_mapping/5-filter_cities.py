#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT B.name"
                " FROM states A JOIN cities B"
                " ON A.id = B.state_id AND A.name = %(username)s"
                " ORDER BY B.id", {'username': argv[4]})

    rows = cur.fetchall()
    for index in range(len(rows)):
        if index != 0:
            print(', ', end='')
        print(rows[index][0], end='')
    print('')
    cur.close()
    db.close()
