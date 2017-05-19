import psycopg2
import os


def open_con():
    try:
        connect_str = "dbname='peter' user='peter' host='localhost' password='Hajtrude2??'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        return conn
    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def printer(cursor):
    rows = cursor.fetchall()
    for row in rows:
        print(" ".join(map(str, row)))


def mentor_names(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT first_name,last_name FROM mentors""")
    printer(cursor)
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(" ".join(map(str, row)))


def miskolc_mentor_nicknames(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT nick_name FROM mentors""")
    rows = cursor.fetchall()
    for row in rows:
        print(" ".join(map(str, row)))


def carol_name_and_phonenum(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name)
                   AS full_name,phone_number FROM applicants WHERE first_name='Carol'""")
    rows = cursor.fetchall()
    for row in rows:
        print(" ".join(map(str, row)))


def girl_from_adipiscingenimmi(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                   FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu'""")
    rows = cursor.fetchall()
    for row in rows:
        print(" ".join(map(str, row)))


def add_new_applicant(conn):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO applicants(first_name, last_name, phone_number, email, application_code)
                   SELECT 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823
                   WHERE NOT EXISTS(SELECT * FROM applicants WHERE application_code=54823)""")


def show_new_applicant(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM applicants WHERE application_code=54823""")
    rows = cursor.fetchall()
    for row in rows:
        print(" ".join(map(str, row)))


def update_phone_num(conn):
    cursor = conn.cursor()
    cursor.execute("""UPDATE applicants SET phone_number='003670/223-7459'
                   WHERE first_name='Jemima' AND last_name='Foreman'""")


def show_jemina_phone(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT phone_number FROM applicants
                   WHERE first_name='Jemima' AND last_name='Foreman'""")
    rows = cursor.fetchall()
    for row in rows:
        print(" ".join(map(str, row)))


def del_mauriseu(conn):
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM applicants
                   WHERE email LIKE '%@mauriseu.net'""")


def main():
    opened_con = open_con()
    table_name = 'applicants'
    running_app = True
    os.system('clear')
    while running_app:
        print("Choose from the following options: " + "\n")
        print("0: Exit")
        print("1: Full name of all the mentors")
        print("2: Nick names of the mentors at Miskolc")
        print("3: Full name and phone number of Carol the applicant")
        print("4: Full name and phone number of Applicant from Adipiscingenimmi")
        print("5: Add Markus Schaffarzyk to the Applicants")
        print("6: Show details of Markus Schaffarzyk the Applicant")
        print("7: Update phone number of Jemina Foreman")
        print("8: Show phone number of Jemina Foreman")
        print("9: Delete Applicants with @mauriseu.net email adress ending" + "\n")
        try:
            chosen_option = int(input("Choose an option: "))
            valid_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            if chosen_option in valid_inputs:
                options = {1: mentor_names,
                           2: miskolc_mentor_nicknames,
                           3: carol_name_and_phonenum,
                           4: girl_from_adipiscingenimmi,
                           5: add_new_applicant,
                           6: show_new_applicant,
                           7: update_phone_num,
                           8: show_jemina_phone,
                           9: del_mauriseu}
                options[chosen_option](opened_con)
            elif chosen_option == 0:
                running_app = False
            else:
                print('Invalid input! Please select from these options: 0,1,2,3,4,5,6,7,8,9')
        except ValueError:
            print('Invalid input! Please select from these options: 0,1,2,3,4,5,6,7,8,9')


if __name__ == '__main__':
    main()
