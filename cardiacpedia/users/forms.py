# Form Based Imports
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_login import current_user
from cardiacpedia.models import User

def check_password(form, field):
    user = User.query.filter_by(email=form.email.data).first()
    #check to see if the password is correct
    if not user.check_password(field.data):
        raise ValidationError('The entered password did not match our records')

def validate_password(form, field):
    #check to see if the password is correct
    if not current_user.check_password(field.data):
        raise ValidationError('The entered password did not match our records')

def validate_username(form, field):
    # Check if not None for that username!
    if current_user.username == field.data:
        pass
    elif User.query.filter_by(username=field.data).first():
        raise ValidationError('Sorry, that username is taken!')

def validate_email(form, field):
    # Check if not None for that user email!
    if current_user.email == field.data:
        pass
    elif User.query.filter_by(email=field.data).first():
        raise ValidationError('Your email has been registered already!')



class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email cannot be left blank'), Email(message='Please enter a valid email address')])
    password = PasswordField('Password', validators=[check_password, DataRequired(message='Passwords Must Match!')])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email cannot be left blank'),Email(message='Please enter a valid email address')])
    username = StringField('Username', validators=[DataRequired(message='Username cannot be left blank')])
    password = PasswordField('Password', validators=[DataRequired(message='Password cannot be left blank'), EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired(message='This field cannot be left blank')])
    submit = SubmitField('Register!')

    def validate_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, field):
        # Check if not None for that username!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Sorry, that username is taken!')


class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[validate_email, DataRequired(message='Email cannot be left blank'),Email(message='Please enter a valid email address')])
    username = StringField('Username', validators=[validate_username, DataRequired(message='Username cannot be left blank')])
    curr_pass = PasswordField('Password', validators=[validate_password, DataRequired(message='Password cannot be left blank')])
    password = PasswordField('New Password', validators=[EqualTo('pass_confirm', message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm Password')
    submit = SubmitField('Update')
