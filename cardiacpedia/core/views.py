from flask import render_template, url_for, redirect, Blueprint
from cardiacpedia.devices.forms import *
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from cardiacpedia.core.forms import Contact

core = Blueprint('core', __name__)

@core.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('devices.home'))
    else:
        return render_template('index.html', page_title="CardiacBook - The Ultimate ICD Assistant")


@core.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact()
    if form.validate_on_submit():
        flash('Thank you for getting in touch with us')
        return redirect(url_for('core.index'))

    return render_template('connect.html', page_title="Connect", form=form)
