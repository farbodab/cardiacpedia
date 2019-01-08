from flask import render_template
from cardiacpedia import db,login_manager, requires_access_level
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

ACCESS = {
    'guest': 0,
    'unpaid': 1,
    'paid':2,
    'admin': 3
}

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        email = db.Column(db.String(255), nullable=False, unique=True, index=True)
        password_hash = db.Column(db.String(255))
        access = db.Column(db.String(5))
        customer_id = db.Column(db.String(255))
        plan = db.Column(db.String(255))
        plan_id = db.Column(db.String(255))

        def __init__(self, email, password, access=ACCESS['unpaid'], customer_id='', plan='', plan_id=''):
            self.email = email
            self.password_hash = generate_password_hash(password)
            self.access = access
            self.customer_id = customer_id
            self.plan = plan
            self.plan_id = plan_id

        def check_password(self,password):
            return check_password_hash(self.password_hash,password)

        def is_admin(self):
            return self.access == ACCESS['admin']

        def allowed(self, access_level):
            return int(self.access) >= access_level


# Define the UserRoles association table
class IPG(db.Model):
    __tablename__ = 'ipg'
    id = db.Column(db.Integer(), primary_key=True)
    manufacturer = db.Column(db.String(255), nullable=False)
    model_number = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255),nullable=True)
    nbg_code = db.Column(db.String(255),nullable=True)
    x_ray = db.Column(db.String(255), nullable=True)
    ra = db.Column(db.String(255), nullable=True)
    rv = db.Column(db.String(255), nullable=True)
    detach = db.Column(db.String(255), nullable=True)
    n_bos = db.Column(db.String(255), nullable=True)
    n_rrt = db.Column(db.String(255), nullable=True)
    m_bos = db.Column(db.String(255), nullable=True)
    m_rrt = db.Column(db.String(255), nullable=True)
    rrt_behaviour = db.Column(db.String(255), nullable=True)
    rrt_longevity = db.Column(db.String(255), nullable=True)

class CRTP(db.Model):
    __tablename__ = 'crtp'
    id = db.Column(db.Integer(), primary_key=True)
    manufacturer = db.Column(db.String(255), nullable=False)
    model_number = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255),nullable=True)
    nbg_code = db.Column(db.String(255),nullable=True)
    x_ray = db.Column(db.String(255), nullable=True)
    ra = db.Column(db.String(255), nullable=True)
    la = db.Column(db.String(255), nullable=True)
    rv = db.Column(db.String(255), nullable=True)
    lv = db.Column(db.String(255), nullable=True)
    detach = db.Column(db.String(255), nullable=True)
    n_bol = db.Column(db.String(255), nullable=True)
    n_eri = db.Column(db.String(255), nullable=True)
    m_bol = db.Column(db.String(255), nullable=True)
    m_eri = db.Column(db.String(255), nullable=True)
    eri_behaviour = db.Column(db.String(255), nullable=True)
    longevity = db.Column(db.String(255), nullable=True)

class ICD(db.Model):
    __tablename__ = 'icd'
    id = db.Column(db.Integer(), primary_key=True)
    manufacturer = db.Column(db.String(255), nullable=False)
    model_number = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255),nullable=True)
    nbg_code = db.Column(db.String(255),nullable=True)
    x_ray = db.Column(db.String(255), nullable=True)
    serial = db.Column(db.String(255), nullable=True)
    ra = db.Column(db.String(255), nullable=True)
    rv = db.Column(db.String(255), nullable=True)
    hv = db.Column(db.String(255), nullable=True)
    detach = db.Column(db.String(255), nullable=True)
    wave = db.Column(db.String(255), nullable=True)
    replacement = db.Column(db.String(255), nullable=True)

class CRTD(db.Model):
    __tablename__ = 'crtd'
    id = db.Column(db.Integer(), primary_key=True)
    manufacturer = db.Column(db.String(255), nullable=False)
    model_number = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255),nullable=True)
    nbg_code = db.Column(db.String(255),nullable=True)
    x_ray = db.Column(db.String(255), nullable=True)
    serial = db.Column(db.String(255), nullable=True)
    ra = db.Column(db.String(255), nullable=True)
    rv = db.Column(db.String(255), nullable=True)
    lv = db.Column(db.String(255), nullable=True)
    hv = db.Column(db.String(255), nullable=True)
    detach = db.Column(db.String(255), nullable=True)
    wave = db.Column(db.String(255), nullable=True)
    replacement = db.Column(db.String(255), nullable=True)

class LV(db.Model):
    __tablename__ = 'lv'
    id = db.Column(db.Integer(), primary_key=True)
    manufacturer = db.Column(db.String(255), nullable=False)
    model_number = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255),nullable=True)
    serial = db.Column(db.String(255), nullable=True)
    sense = db.Column(db.String(255), nullable=True)
    polarity = db.Column(db.String(255), nullable=True)
    fixation = db.Column(db.String(255), nullable=True)
    placement = db.Column(db.String(255), nullable=True)
    insulation = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(255), nullable=True)


class HV(db.Model):
    __tablename__ = 'hv'
    id = db.Column(db.Integer(), primary_key=True)
    manufacturer = db.Column(db.String(255), nullable=False)
    model_number = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255),nullable=True)
    serial = db.Column(db.String(255), nullable=True)
    sense = db.Column(db.String(255), nullable=True)
    high = db.Column(db.String(255), nullable=True)
    sensing = db.Column(db.String(255), nullable=True)
    lead = db.Column(db.String(255), nullable=True)
    placement = db.Column(db.String(255), nullable=True)
    fixation = db.Column(db.String(255), nullable=True)
    insulation = db.Column(db.String(255), nullable=True)
