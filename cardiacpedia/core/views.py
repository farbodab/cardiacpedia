from flask import render_template, url_for, redirect, Blueprint
from cardiacpedia.devices.forms import *
from flask_login import login_user, current_user, logout_user, login_required
from cardiacpedia.core.forms import Contact
import stripe
from cardiacpedia import requires_access_level

stripe_keys = {
  'secret_key': 'pk_test_dtOoNU1AqHUdKNcjSaL7iZ7m',
  'publishable_key': 'sk_test_sUBjEZ7otbSikPzwk3HPVZb0'
}

stripe.api_key = stripe_keys['secret_key']

core = Blueprint('core', __name__)

@core.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.allowed(2):
            return redirect(url_for('devices.home'))
        elif current_user.allowed(1):
            return redirect(url_for('users.pay'))
    else:
        return render_template('index.html', page_title="CardiacBook - The Ultimate ICD Assistant")


@core.route('/contact', methods=['GET', 'POST'])
def contact():
    form = Contact()
    if form.validate_on_submit():
        flash('Thank you for getting in touch with us')
        return redirect(url_for('core.index'))

    return render_template('connect.html', page_title="Connect", form=form)
