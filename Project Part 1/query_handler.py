import psycopg2


def user_datas():
    """Read the nessecery information from the user_file to
    connect to the database, such as dbname, username, password
    """
    with open('user.txt') as file:
        data = file.read()
        data = data.split(',')
        return data


def open_con():
    try:
        connect_str = "dbname={0} user={0} host='localhost' password={1}".format(data[0], data[1])
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
