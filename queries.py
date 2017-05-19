def mentor_names():
    return """SELECT first_name,last_name FROM mentors;"""


def miskolc_mentor_nicknames():
    return """SELECT nick_name FROM mentors;"""


def carol_name_and_phonenum():
    return """SELECT CONCAT(first_name, ' ', last_name)
                   AS full_name,phone_number FROM applicants WHERE first_name='Carol';"""


def girl_from_adipiscingenimmi():
    return """SELECT CONCAT(first_name, ' ', last_name) AS full_name, phone_number
                   FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';"""


def add_new_applicant():
    return """INSERT INTO applicants(first_name, last_name, phone_number, email, application_code)
                   SELECT 'Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823
                   WHERE NOT EXISTS(SELECT * FROM applicants WHERE application_code=54823);"""


def show_new_applicant():
    return """SELECT * FROM applicants WHERE application_code=54823;"""


def update_phone_num():
    return """UPDATE applicants SET phone_number='003670/223-7459'
                   WHERE first_name='Jemima' AND last_name='Foreman';"""


def show_jemina_phone():
    return """SELECT phone_number FROM applicants
                   WHERE first_name='Jemima' AND last_name='Foreman';"""


def del_mauriseu():
    return """DELETE FROM applicants
                   WHERE email LIKE '%@mauriseu.net';"""
