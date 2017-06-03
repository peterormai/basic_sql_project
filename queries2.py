import psycopg2


def user_datas():
    """
    Read the nessecery information from the user_file to
    connect to the database, such as dbname, username, password
    """
    with open('user.txt') as file:
        data = file.read()
        data = data.split(',')
        return data


def fetch_database(query, tuple_paramerters=None):
    """
    Connects to the database to retrieve data, then
    returns it.
    """
    try:
        data = user_datas()
        connect_str = "dbname={0} user={0} host='localhost' password={1}". format(data[0], data[1])
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(query, tuple_paramerters)
        rows = cursor.fetchall()
        return rows
    except psycopg2.DatabaseError as exception:
        print(exception)
    finally:
        if conn:
            conn.close()


def mentors_and_schools():
    """
    Returns the name of the mentors plus the name and country of the school ordered by the mentors id.
    """
    query_result = fetch_database("""SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS name, schools.name, schools.country
                                    FROM mentors LEFT JOIN schools ON mentors.city=schools.city ORDER BY mentors.id;""")
    table_titles = ["Mentor", "School", "Country"]
    result = [query_result, table_titles]
    return result


def mentors_and_all_schools():
    """
    Returns the name of the mentors plus the name and country of the school ordered by the mentors id column.
    BUT include all the schools, even if there's no mentor yet!
    """
    query_result = fetch_database("""SELECT CONCAT(mentors.first_name, ' ', mentors.last_name) AS name, schools.name, schools.country
                                    FROM mentors FULL JOIN schools ON mentors.city=schools.city ORDER BY mentors.id;""")
    table_titles = ["Mentor", "School", "Country"]
    result = [query_result, table_titles]
    return result


def mentors_by_country():
    """
    Returns the number of the mentors per country ordered by the name of the countries.
    """
    query_result = fetch_database("""SELECT schools.country, COUNT(mentors.last_name) FROM schools LEFT JOIN mentors
                                    ON schools.city=mentors.city GROUP BY schools.country ORDER BY schools.country;""")
    table_titles = ["Country", "Number of mentors"]
    result = [query_result, table_titles]
    return result


def contacts():
    """
    Returns the name of the school plus the name of contact person at the school ordered by the name of the school.
    """
    query_result = fetch_database("""SELECT schools.name, CONCAT(mentors.first_name, ' ', mentors.last_name) AS name
                                    FROM schools LEFT JOIN mentors ON schools.contact_person=mentors.id
                                    ORDER BY schools.name;""")
    table_titles = ["School", "Contact person"]
    result = [query_result, table_titles]
    return result


def applicants():
    """
    Returns the first name and the code of the applicants plus the creation_date of the application
    ordered by the creation_date in descending order.
    """
    query_result = fetch_database("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                                    FROM applicants LEFT JOIN applicants_mentors
                                    ON applicants.id=applicants_mentors.applicant_id
                                    WHERE applicants_mentors.creation_date > '2016-01-01'
                                    ORDER BY applicants_mentors.creation_date DESC;""")
    table_titles = ["Applicant", "Application code", "Creation date"]
    result = [query_result, table_titles]
    return result


def applicants_and_mentors():
    """
    Returns the first name and the code of the applicants plus the name of the assigned mentor
    ordered by the applicants id column.
    Show all the applicants, even if they have no assigned mentor in the database!
    """
    query_result = fetch_database("""SELECT applicants.first_name, applicants.application_code,
                                    CONCAT_WS(mentors.first_name, ' ', mentors.last_name)
                                    FROM applicants LEFT JOIN applicants_mentors
                                    ON applicants.id=applicants_mentors.applicant_id
                                    LEFT JOIN mentors ON applicants_mentors.mentor_id=mentors.id;""")
    table_titles = ["Applicant", "Application code", "Assigned mentor"]
    result = [query_result, table_titles]
    return result
