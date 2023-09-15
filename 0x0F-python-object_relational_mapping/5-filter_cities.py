#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASS,
                         db=DB,
                         charset="utf8")

    cursor = db.cursor()
    query = " ".join(["SELECT c.name FROM cities c, states st",
                      "WHERE c.state_id = st.id",
                      "AND st.name = %(name)s",
                      "ORDER BY c.id"])

    cursor.execute(query, {'name': state_name})
    rows = cursor.fetchall()
    for i in range(len(rows)):
        if i != len(rows) - 1:
            print(rows[i][0], end=", ")
        else:
            print(rows[i][0])

    cursor.close()
    db.close()
