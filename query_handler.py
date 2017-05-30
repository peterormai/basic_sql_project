import psycopg2


def open_con():
    try:
        connect_str = "dbname='peter' user='peter' host='localhost' password='Hajtrude2??'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        return conn
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def query_result(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    try:
        rows = cursor.fetchall()
        print("RESULT:" + "\n")
        for row in rows:
            print(" ".join(map(str, row)))
    except:
        print("DONE!" + "\n")


# def print_query_result(cursor):
#     rows = cursor.fetchall()
#     print("RESULT:" + "\n")
#     for row in rows:
#         print(" ".join(map(str, row)))
