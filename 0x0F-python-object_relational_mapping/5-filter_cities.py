#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=argv[1], passwd=argv[2],
                                    db=argv[3], charset="utf8")
    cursor = db_connection.cursor()
    cursor.execute("SELECT c.name FROM cities AS c\
                    INNER JOIN states AS s ON s.id = c.state_id\
                    WHERE s.name LIKE %s ORDER BY c.id ASC", (argv[4],))
    query_rows = cursor.fetchall()
    myList = []
    for row in query_rows:
        for col in row:
            myList.append(col)
    print(*myList, sep=', ')
    cursor.close()
    db_connection.close()
