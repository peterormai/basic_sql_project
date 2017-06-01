from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
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
    return render_template('list.html', links=links, menu=menu, title=title)


@app.route('/mentors')
def show_mentors_and_schools():
    data_list = queries2.mentors_and_schools()
    title = "Mentors & schools"
    return render_template('main.html', data_list=data_list, title=title)


@app.route('/all-school')
def show_mentors_and_all_schools():
    data_list = queries2.mentors_and_all_schools()
    title = "Mentors & all schools"
    return render_template('main.html', data_list=data_list, title=title)


@app.route('/mentors-by-country')
def show_mentors_by_country():
    data_list = queries2.mentors_by_country()
    title = "Mentors by country"
    return render_template('main.html', data_list=data_list, title=title)


@app.route('/contacts')
def show_contacts():
    data_list = queries2.contacts()
    title = "Contacts"
    return render_template('main.html', data_list=data_list, title=title)


@app.route('/applicants')
def show_applicants():
    data_list = queries2.applicants()
    title = "Applicants"
    return render_template('main.html', data_list=data_list, title=title)


@app.route('/applicants-and-mentors')
def show_applicants_and_mentors():
    data_list = queries2.applicants_and_mentors()
    title = "Applicants and mentors"
    return render_template('main.html', data_list=data_list, title=title)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
