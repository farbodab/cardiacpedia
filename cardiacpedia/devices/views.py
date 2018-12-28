from flask import render_template, url_for, flash, redirect, request, Blueprint, render_template_string
from cardiacpedia import db
from cardiacpedia.models import user_manager
from werkzeug.security import generate_password_hash,check_password_hash
from cardiacpedia.models import User, Role, UserRoles
from cardiacpedia.users.forms import Remove_User_Roles, Add_User_Roles, Add_Roles, Remove_Roles, Remove_Users
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

devices = Blueprint('devices', __name__)

################################################################################
##############################View Table########################################
################################################################################
@devices.route('/devices')
@login_required
def main_table():
    return render_template('/devices.html', page_title='Devices')
