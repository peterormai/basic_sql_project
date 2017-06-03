from flask import Flask
from flask import render_template
import queries2


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    """
    Error handling for wrong DNS address request.
    """
    return render_template('404.html')


@app.route('/')
def index():
    """
    It shows a list of links which are pointing to specific roots.
    """
    title = "Application process "
    links = {'mentors': 'mentors',
             'schools': 'all-school',
             'mentors_by_country': 'mentors-by-country',
             'contacts': 'contacts',
             'applicants': 'applicants',
             'applicants_and_mentors': 'applicants-and-mentors'}
    menu = ['Show mentors and schools',
            'Show mentors and all schools',
            'Show mentors by country',
            'Show contacts',
            'Show applicants',
            'Show applicants and mentors']
    return render_template('index.html', links=links, menu=menu, title=title)


@app.route('/mentors')
def show_mentors_and_schools():
    """
    Shows the result of the mentors and schools query at the given page.
    """
    data_list = queries2.mentors_and_schools()[0]
    table_titles = queries2.mentors_and_schools()[1]
    title = "Mentors & schools"
    return render_template('pages.html', data_list=data_list, title=title, table_titles=table_titles)


@app.route('/all-school')
def show_mentors_and_all_schools():
    """
    Shows the result of the mentors and all schools query at the given page.
    """
    data_list = queries2.mentors_and_all_schools()[0]
    table_titles = queries2.mentors_and_all_schools()[1]
    title = "Mentors & all schools"
    return render_template('pages.html', data_list=data_list, title=title, table_titles=table_titles)


@app.route('/mentors-by-country')
def show_mentors_by_country():
    """
    Shows the result of the mentors by country query at the given page.
    """
    data_list = queries2.mentors_by_country()[0]
    table_titles = queries2.mentors_by_country()[1]
    title = "Mentors by country"
    return render_template('pages.html', data_list=data_list, title=title, table_titles=table_titles)


@app.route('/contacts')
def show_contacts():
    """
    Shows the result of the contacts query at the given page.
    """
    data_list = queries2.contacts()[0]
    table_titles = queries2.contacts()[1]
    title = "Contacts"
    return render_template('pages.html', data_list=data_list, title=title, table_titles=table_titles)


@app.route('/applicants')
def show_applicants():
    """
    Shows the result of the applicants query at the given page.
    """
    data_list = queries2.applicants()[0]
    table_titles = queries2.applicants()[1]
    title = "Applicants"
    return render_template('pages.html', data_list=data_list, title=title, table_titles=table_titles)


@app.route('/applicants-and-mentors')
def show_applicants_and_mentors():
    """
    Shows the result of the applicants and mentors query at the given page.
    """
    data_list = queries2.applicants_and_mentors()[0]
    table_titles = queries2.applicants_and_mentors()[1]
    title = "Applicants and mentors"
    return render_template('pages.html', data_list=data_list, title=title, table_titles=table_titles)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
