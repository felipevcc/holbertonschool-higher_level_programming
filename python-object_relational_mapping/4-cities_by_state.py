#!/usr/bin/python3
"""MySQLdb script"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(f"SELECT c.id, c.name, st.name \
        FROM cities AS c \
        JOIN states AS st \
            ON c.state_id = st.id \
        ORDER BY c.id")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
