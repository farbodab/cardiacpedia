from flask import render_template, url_for, flash, redirect, request, Blueprint, render_template_string
from cardiacpedia import db
from cardiacpedia.models import user_manager
from werkzeug.security import generate_password_hash,check_password_hash
from cardiacpedia.models import User, Role, UserRoles
from cardiacpedia.users.forms import Remove_User_Roles, Add_User_Roles, Add_Roles, Remove_Roles, Remove_Users
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

users = Blueprint('users', __name__)



################################################################################
##############################View Users########################################
################################################################################
@users.route('/admin/users/view_users')
@roles_required('Admin')    # Use of @roles_required decorator
def admin_users_view_users():
    """
    Allows the admin to view all users in the system
    """
    users = User.query.order_by(User.id, User.email, User.first_name, User.last_name).all()
    return render_template('/Admin/view_users.html', users=users)

################################################################################
##############################Remove Users########################################
################################################################################
@users.route('/admin/users/remove_users', methods=['GET', 'POST'])
@roles_required('Admin')    # Use of @roles_required decorator
def admin_users_remove_users():

    form = Remove_Users()

    if form.validate_on_submit():
        User.query.filter_by(user_id=form.user_id.data).delete()
        db.session.commit()
        flash('User has been removed from the database.')
        return redirect(url_for('users.admin_users_view_users'))

    return render_template('/Admin/remove_users.html', form=form)

################################################################################
##############################View Roles########################################
################################################################################

@users.route('/admin/users/view_roles')
@roles_required('Admin')    # Use of @roles_required decorator
def admin_users_view_roles():
    """
    Allows the admin to view all roles in the system
    """
    roles = Role.query.order_by(Role.id, Role.name).all()
    return render_template('/Admin/view_roles.html', roles=roles)


################################################################################
##############################Add Roles########################################
################################################################################

@users.route('/admin/users/add_roles', methods=['GET', 'POST'])
@roles_required('Admin')    # Use of @roles_required decorator
def admin_users_add_roles():

    form = Add_Roles()


    if form.validate_on_submit() and not Role.query.filter_by(name=form.role_name.data).first():
        roles = Role(
            name=form.role_name.data,
        )
        db.session.add(roles)
        db.session.commit()
        flash('Roles have been added.')
        return redirect(url_for('users.admin_users_view_roles'))

    return render_template('/Admin/add_roles.html', form=form)

################################################################################
##############################Remve Roles########################################
################################################################################
@users.route('/admin/users/remove_roles', methods=['GET', 'POST'])
@roles_required('Admin')    # Use of @roles_required decorator
def admin_users_remove_roles():

    form = Remove_Roles()

    if form.validate_on_submit():
        Role.query.filter_by(id=form.role_id.data).delete()
        db.session.commit()
        flash('Roles has been removed.')
        return redirect(url_for('users.admin_users_view_roles'))

    return render_template('/Admin/remove_roles.html', form=form)


################################################################################
##############################Add User Roles#####################################
################################################################################

@users.route('/admin/users/add_user_roles', methods=['GET', 'POST'])
@roles_required('Admin')    # Use of @roles_required decorator
def admin_users_add_user_roles():

    form = Add_User_Roles()

    if form.validate_on_submit():
        user_roles_new = UserRoles(
            user_id=form.user_id.data,
            role_id = form.role_id.data,
        )
        db.session.add(user_roles_new)
        db.session.commit()
        flash('Roles have been added to the user.')
        return redirect(url_for('users.admin_users_view_users'))

    return render_template('/Admin/add_user_roles.html', form=form)



################################################################################
##############################Remove User Roles#################################
################################################################################

@users.route('/admin/users/remove_user_roles', methods=['GET', 'POST'])
@roles_required('Admin')    # Use of @roles_required decorator
def admin_users_remove_user_roles():

    form = Remove_User_Roles()

    if form.validate_on_submit():
        UserRoles.query.filter_by(user_id=form.user_id.data, role_id=form.role_id.data).delete()
        db.session.commit()
        flash('Roles has been removed from the user.')
        return redirect(url_for('users.admin_users_view_users'))

    return render_template('/Admin/remove_user_roles.html', form=form)
