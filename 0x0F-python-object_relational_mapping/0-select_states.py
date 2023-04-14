#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db_connection = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                    db=argv[3])
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db_connection.close()
