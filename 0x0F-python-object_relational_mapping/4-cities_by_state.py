#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=argv[1], passwd=argv[2],
                                    db=argv[3], charset="utf8")
    cursor = db_connection.cursor()
    cursor.execute("SELECT c.id, c.name, s.name FROM cities AS c\
                    INNER JOIN states AS s ON s.id = c.state_id\
                    ORDER BY c.id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print("{}".format(row))
    cursor.close()
    db_connection.close()
