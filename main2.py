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


# @app.route('/')
# def index():
#     """
#     It shows a list of links which are pointing to specific roots.
#     """
#     title = "Application process "
#     top_menu = ['ID', 'Created at', 'Views', 'Votes', 'Title', 'Edit', 'Delete', "Like", "Dislike"]
#     return render_template('main.html', data_list=data_list, title=title, top_menu=top_menu)


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


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
