from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    #home page view
    return render_template('index.html', page_title="Home")

@core.route('/about')
def about():
    #about page
    return render_template('about.html', page_title="About Us")
