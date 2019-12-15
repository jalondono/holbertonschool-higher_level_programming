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

    cur.execute("""SELECT cities.name
                       FROM cities JOIN states
                       ON cities.state_id = states.id
                       WHERE states.name = %s
                       ORDER BY cities.id;""", (argv[4],))
    rows = cur.fetchall()
    for row in range(len(rows)):
        if row != len(rows) - 1:
            print('{}, '.format(rows[row][0]), end='')
        else:
            print('{}'.format(rows[row][0]))
    cur.close()
    db.close()
