#!/usr/bin/python3
"""   lists all states name start with N from the db hbtn_0e_0_usa: """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=argv[1], passwd=argv[2],
                                    db=argv[3], charset="utf8")
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states\
                    WHERE name LIKE 'N%'\
                    ORDER BY states.id")
    query_rows = cursor.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db_connection.close()
