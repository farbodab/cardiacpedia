from flask import render_template, url_for, redirect, Blueprint
from cardiacpedia.devices.forms import *
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

core = Blueprint('core', __name__)

@core.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('devices.finder'))
    else:
        return render_template('index.html', page_title="CardiacPedia - The Ultimate ICD Assistant")
