from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    #home page view
    return render_template('index.html', page_title="Home")
