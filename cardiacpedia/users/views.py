from flask import render_template, url_for, flash, redirect, request, Blueprint, render_template_string
from cardiacpedia import db
from cardiacpedia.models import user_manager
from werkzeug.security import generate_password_hash,check_password_hash
from cardiacpedia.models import User
from cardiacpedia.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

users = Blueprint('users', __name__)


# The Admin page requires an 'Admin' role.
@users.route('/admin')
@roles_required('Admin')    # Use of @roles_required decorator
def admin_page():
    return render_template_string("""
            {% extends "base.html" %}
            {% block content %}
                <h2>{%trans%}Admin Page{%endtrans%}</h2>
            {% endblock %}
            """)
