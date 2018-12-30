from flask import render_template
from cardiacpedia import db, app, template_dir
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin

class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

        # User authentication information. The collation='NOCASE' is required
        # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
        email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
        email_confirmed_at = db.Column(db.DateTime())
        password = db.Column(db.String(255), nullable=False, server_default='')

        # User information
        first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
        last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')

        # Define the relationship to Role via UserRoles
        roles = db.relationship('Role', secondary='user_roles')

# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

# Define the UserRoles association table
class IPG(db.Model):
    __tablename__ = 'ipg'
    id = db.Column(db.Integer(), primary_key=True)
    manufacturer = db.Column(db.String(255, collation='NOCASE'), nullable=False)
    model_number = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    name = db.Column(db.String(255, collation='NOCASE'),nullable=True)
    nbg_code = db.Column(db.String(255, collation='NOCASE'),nullable=True)
    x_ray = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    ra = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    rv = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    detach = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    n_bos = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    n_rrt = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    m_bos = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    m_rrt = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    rrt_behaviour = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    rrt_longevity = db.Column(db.String(255, collation='NOCASE'), nullable=True)

class CRTP(db.Model):
    __tablename__ = 'crtp'
    id = db.Column(db.Integer(), primary_key=True)
    manufacturer = db.Column(db.String(255, collation='NOCASE'), nullable=False)
    model_number = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    name = db.Column(db.String(255, collation='NOCASE'),nullable=True)
    nbg_code = db.Column(db.String(255, collation='NOCASE'),nullable=True)
    x_ray = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    ra = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    la = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    rv = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    lv = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    detach = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    n_bol = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    n_eri = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    m_bol = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    m_eri = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    eri_behaviour = db.Column(db.String(255, collation='NOCASE'), nullable=True)
    longevity = db.Column(db.String(255, collation='NOCASE'), nullable=True)


user_manager = UserManager(app, db, User)
